---
title: USSD Overview
description: USSD implementation and test
keywords: USSD,Unstructured Supplementary Service Data 
ms.date: 03/01/2021
ms.localizationpriority: medium
---
# USSD Overview

Unstructured Supplementary Service Data (USSD) is a communication protocol used by Global System for Mobile Communications (GSM) devices to communicate with mobile network operators (typically referred to as simply "MO").

To understand USSD it is helpful to compare it to its most closely-related sibling: short message service (SMS). USSD and SMS are both GSM standards, meaning they were introduced as features in the second generation of mobile devices. In contrast with SMS however, USSD is a session-based connection. While SMS is used for short session-less messaging, USSD is typically used for command and control of a mobile device. As it is a necessary to maintain a session, USSD does not support store-and-forward capability as SMS does. Both USSD and SMS messages are sent with 7-bit GSM-compliant characters, but USSD maxes out at 184 characters in contrast with 160 for SMS.

USSD messages may be sent from a mobile phone by opening the dialer and typing a code. Not all codes are supported by every phone or MO. In some cases, the phone software or operating system may prevent manually sending codes. One required code that must be implemented is *#06#. This code returns the International Mobile Equipment Identifier (IMEI) of the modem, but some phones will prevent you from dialing this directly. If you follow conventional means of locating the IMEI of the modem through your phone's settings, that number was retrieved using this code.

If the phone hardware can directly handle a code's command like in the IMEI example, no network session will be initiated. Other codes that require network communication will open a session and then send a message consisting of a command and any necessary parameters, if applicable. One example of this is a code which checks your current balance and plan status with the MO. 

USSD in Windows is implemented as a WinRT API surface. The implementation classes of this interface serve as the state machine for USSD sessions, but ultimately rely on WWAN Service to do the heavy lifting. These APIs are implemented with a factory pattern.


## Implementing USSD
A key thing to remember is that the public facing API is defined by the IDL. Implementation can be confusing because of this, especially if you are unfamiliar with WinRT. Part of the confusion comes from the seemingly ambiguous use of the word 'factory'. A factory can refer to either a class implementation of a static interface or a true factory that provides an activatable interface to a runtime class.

This topic reviews WinRT concepts and then describes the implementation based on these concepts. You may always refer to the IDL for further clarification.

Interfaces

Interfaces define the Application Binary Interface (ABI). They describe the functions that you can call on any class that implements the interface.

Runtime Classes

These are the actual classes. They represent, by name, what is ultimately exposed as class names to the ABI. Each runtime class may have zero or more interfaces (but must declare at least one default interface if it has one or more interfaces), zero or more static interfaces, and an activatable tag if necessary. Each of these interfaces are implemented in different files as different "Impl" classes yet they will appear to be a single, unified class to the ABI.

A typical interface appears as instance methods on an existing object.

A static interface appears to the client as static methods on the runtime class itself.

An activatable tag defines the factory interface that will produce an instance of a runtime class. This is completely obfuscated to the client, appearing as a constructor for that runtime class.

### USSD Implementation

![Diagram showing USSD implementation.](images/ussd_implement.png?raw=true "implement_ussd_img")

## Flow: Open, Send, Receive, Close.
### Open, Send
![Flow diagram for USSD request with reply.](images/ussd_request_with_reply.png?raw=true "resume_ussd_img")
1) The client uses one of the static functions UssdSession.CreateFromNetworkAccountId or UssdSession.CreateFromNetworkInterfaceId to create the UssdSession object.
2) Regardless of the API called, a network interface ID is required to initialize a UssdSession. In the case of *NetworkAccountID, steps are taken to retrieve the network interface ID from the Account ID.
CreateInternal() is called to create a instance of UssdSession and invoke Initialize() on the newly-created instance. During the initialization steps, a worker thread is spun up and an event handle to trigger events for the thread is created. Steps 3 and 4 also take place during the instance's Initialize().
3) Initialize() is called on the WwanWrapper member object. This function accepts a static callback function as well as a context to allow the static function to map the callback to an object context.
4) WwanWrapper opens a handle to WwanService, enumerates interfaces, and subscribes to USSD notifications by providing a static callback function pointer and "this" as context.
5) The UssdSession object is returned to the client.
6) The client constructs a new UssdMessage by invoking the constructor with a message string. WinRT obfuscates the UssdMessageFactory in this process.
7) The client invokes SendMessageAndGetReplyAsync on the session object, passing the UssdMessage instance.
8) At this time SendMessageAndGetReplyAsync creates a special operation object called UssdSendMessageAndGetReplyOperation. From the its name, it appears that the object encapsulates the logic of a single message being sent down the stack (and waiting for reply), but this is not the case. WinRT requires a special out parameter for asynchronous operations, which we can see as the 2nd parameter on the definition for this function. 
    ```
    HRESULT SendMessageAndGetReplyAsync(
                [in] UssdMessage* message,
                [out, retval] Windows.Foundation.IAsyncOperation<UssdReply>** asyncInfo);
    ```
    It is the IUssdSendMessageAndGetReplyOperation, a named interface through typedef, that satisfies this parameter by promising that this operation will inevitably return a UssdReply. This interface is not defined in the IDL, but is implemented by the UssdSendMessageAndGetReplyOperationImpl class. Note that the header for this class has a special extension:
    ```
    class UssdSendMessageAndGetReplyOperationImpl :
        public Microsoft::WRL::RuntimeClass<
            Windows::Networking::NetworkOperators::IUssdSendMessageAndGetReplyOperation,
            Windows::Internal::AsyncBaseFTM<IUssdSendMessageAndGetReplyCompletedHandler, Microsoft::WRL::SingleResult>>
    ```
    The UssdSendMessageAndGetReplyOperation object allows WinRT to obfuscate the complexities of this asynchronous operation and all of the compartmentalization and memory proxying that goes along with it. For more information, see [SendMessageAndGetReplyAsync](/uwp/api/windows.networking.networkoperators.ussdsession.sendmessageandgetreplyasync).

    For now, understand that the asynchronous operation described above simply calls back into the UssdSession object where the logic for this operation is actually contained. We can visualize for simplicity that the UssdSession itself encapsulates the work here. We can now assert that, despite the asynchronous nature, only one UssdMessage may be sent at a time.
    
    What the SendMessageAndGetReplyAsync function actually does:

    * The UssdSession object changes to a busy state, stores the content of the UssdMessage, and fires off the asynchronous action.
    * OnOperationStart() is the entry point for the asynchronous logic. Assume for this scenario that there is no active session. This function creates a WWAN_USSD_REQUEST object with RequestType=WwanUssdRequestInitiate.
    * Steps 9 and 10 occur as actions taken by this function.
        
9) m_wwanWrapper.SendRequest is invoked to handle the work of passing the message to WwanService.
10) WwanWrapper uses the WwanService handle to invoke WwanService APIs to carry out the action.
        
### Receive
![Flow diagram for USSD receive.](images/ussd_resume.png?raw=true "resume_ussd_img")

After step 10, we are left in a state where a request was sent to WwanService to initialize a new USSD session and send a USSD message under that session. After some time, the reply will be available.

11) WwanService will invoke the static callback function provided in step 4 with the context that was also attached.
12) The context will be used to retrieve the WwanWrapper instance and invoke NotificationCallback().
13) WwanWrapper will follow the same pattern as step 11, invoking a static callback to UssdSession, providing the context stored in step 3.
14) Similar to step 12, the context is used to invoke the callback on an instance of UssdSession.
15) The UssdSession stores the WWAN_USSD_EVENT (under a lock) and notifies the worker thread to handle the event.
16) HandleOperationReply() takes the existing UssdSendMessageAndGetReplyOperationImpl object and passes the event data to its internal handler.
17) The operation will construct and UssdReply and invoke FireCompletion() to mark the async action as finished.
18) WinRT obfuscates the completion of the asynchronous action to the client. (Either they have awaited the action or have callback logic.)

More messages can be sent under the same session. If the session was maintained, the future RequestType will be WwanUssdRequestContinue.

### Close
![Flow diagram for USSD close.](images/ussd_resume2.png?raw=true "resume_ussd_img")
After step 18, the client has received the reply to their UssdMessage. They may or may not have continued to use the active UssdSession to send additional messages. We will assume that at some point in the future, the client will manually invoke Close() on the UssdSession. If the client does not explicitly invoke Close(), it will be called during the destructor of UssdSession.

19) Client invokes Close() on the UssdSession instance.
20) A WWAN_USSD_REQUEST is created with RequestType=WwanUssdRequestCancel.
21) The request is sent to m_wwanWrapper as in step 9.
22) The request is sent to WwanService as in step 10.

The result of this request is unimportant. For all intents and purposes, the session is closed. Even in the extreme edge case where the message is somehow never delivered, a new USSD session will always override an existing session.


## Hardware Lab Kit (HLK) Tests
See [Steps for installing HLK](https://microsoft.sharepoint.com/teams/HWKits/SitePages/HWLabKit/Manual%20Controller%20Installation.aspx). 

In HLK Studio connect to the device Cellular modem driver and run the test: [Win6_4.MB.GSM.Data.TestUssd](/windows-hardware/test/hlk/testref/17ae6fea-6244-442d-b977-6367d1ae441e).

## MB USSD Troubleshooting Guide
- Collect and decod the logs using the instructions in [MB Collecting Logs](mb-collecting-logs.md).

- Keywords for filtering
  1. OID_WWAN_USSD 
  1. NDIS_STATUS_WWAN_USSD
  1. WWAN_USSD_REQUEST
  1. WWAN_USSD_EVENT

## See Also
[MB USSD Operations](mb-ussd-operations.md)

