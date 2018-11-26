---
title: Using Custom WMI Events
description: Using Custom WMI Events
ms.assetid: 00354e0b-a652-44e9-8b2b-fd755cc05fec
keywords: ["WMI WDK kernel , event tracking", "events WDK WMI", "tracing WDK WMI", "sending WMI events", "event blocks WDK WMI", "notifications WDK WMI", "event consumer providers WDK WMI", "custom events WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Custom WMI Events





Some classes of drivers are required to support certain WMI event classes. Drivers can also design their own custom WMI event classes. Custom WMI events offer a way for a driver to pass data back to a user-mode component. A user-mode component receives WMI events through WMI COM interfaces.

An application can receive event notifications as follows:

-   Use the **CoCreateInstance** routine to get a pointer to an **IWbemLocator** object.

-   Use the **IWbemLocator** pointer to connect to the WMI server process. The **IWBemLocator::ConnectServer** method call provides you with a pointer to an **IWbemServices** object.

-   Use the **IWbemServices** object to query for the event types you are interested in. The **IWbemServices::ExecNotificationQuery** method allows you to specify an event query in the WMI Query Language (WQL).

-   An application can also register to receive WMI events asynchronously, by implementing the **IWbemObjectSink** interface. The application uses the **IWbemServices::ExecNotificationQueryAsync** method to register for asynchronous notification of events. When matching events occur, the system uses the **IWbemObjectSink::Indicate** method to notify the application of the events that have occurred.

You can also implement a user-mode WMI *event consumer provider*. This is a user-mode component that WMI can automatically load when events of a specified type occur.

-   Include an instance of the **\_\_EventConsumerProviderRegistration** WMI class in the MOF data for your user-mode component.

-   Implement the **IWbemUnboundObjectSink** interface for each WMI event class you want to receive notifications of.

-   Implement the **IWbemEventConsumerProvider** interface to specify the event classes the component receives notifications of, and the associated **IWbemUnboundObjectSink** implementations.

-   Implement the **IWbemProviderInit** interface that initializes your component as an event consumer.

More information about receiving WMI events and the **IWbemXxx** COM interfaces can be found in the Microsoft Windows SDK documentation.

WMI events are not the only way to notify user-mode applications when particular situations occur. A driver could implement an IOCTL that an application could use to poll for notification. The driver and application could share a notification event object (see [Event Objects](event-objects.md)) to signal that a particular situation has occurred.

WMI events have some advantages over these other methods:

-   If user-mode applications poll for events faster than the driver can respond, then the driver may have many IOCTLs pending.

-   You can ameliorate the previous problem by using a notification event object to notify a user-mode application, but notification events can only signal that an event has occurred. The application must still use an IOCTL to get any additional data. The next two issues still apply.

-   If multiple applications poll the driver for events, the driver would need to maintain state to determine which applications had received which events.

-   Some drivers, such as SCSI miniport and NDIS miniport drivers, cannot receive IOCTLs.

WMI events do have the disadvantage that the user-mode code you must provide is considerably more complicated than that for the other methods.

 

 




