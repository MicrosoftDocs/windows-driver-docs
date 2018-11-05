---
Description: Supporting the Service Commands
title: Supporting the Service Commands
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting the Service Commands


WPD issues service commands when an application calls several methods that are found in the service interfaces that are supported by the WPD API.

In the sample driver, these service commands are first processed by the **WpdService::DispatchMessage** method. This method examines the given command and forwards it to the appropriate handler. The sample driver forwards any of the capability commands to a handler in the *WpdServiceCapabilities.cpp* module. The sample driver forwards any of the method commands to a handler in the *WpdServiceMethods.cpp* module.

The following table describes the commands that are supported by the service module, together with their descriptions and handlers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Description/Handler</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_METHODS_START_INVOKE</td>
<td align="left"><p>Description: Issued when an application calls either the <strong>IPortableDeviceServiceMethods::Invoke</strong> or the <strong>IPortableDeviceServiceMethods::InvokeAsync</strong> method.</p>
<p>Handler:<strong>WpdServiceMethods::OnStartInvoke</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_METHODS_END_INVOKE</td>
<td align="left"><p>Description: Issued when a method, that was invoked by the application, has finished running. (WPD issues this command for both synchronous and asynchronous methods.)</p>
<p>Handler: <strong>WpdServiceMethods::OnEndInvoke</strong></p></td>
</tr>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_METHODS_CANCEL_INVOKE</td>
<td align="left"><p>Description: Issued when an application calls the <strong>IPortableDeviceServiceMethods::Cancel</strong> method to cancel a method invocation that has not completed.</p>
<p>Handler: <strong>WpdServiceMethods::OnCancelInvoke</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_COMMON_GET_SERVICE_OBJECT_ID</td>
<td align="left"><p>Description: Issued when an application calls the <strong>IPortableDeviceService::GetServiceObjectId</strong> method to retrieve the object identifier of the current service.</p>
<p>Handler: <strong>OnGetServiceObjectID</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="Supporting_the_Service-Capability_Commands"></span><span id="supporting_the_service-capability_commands"></span><span id="SUPPORTING_THE_SERVICE-CAPABILITY_COMMANDS"></span>Supporting the Service-Capability Commands


WPD applications use the methods that are found in the **IPortableDeviceServiceCapabilities** interface to discover the functionality that is offered by a service. By using the methods in this interface, an application can retrieve descriptions of supported methods, events, and formats. And, an application can retrieve even more specific data such as the attributes of a particular parameter for a given method.

In the sample driver, the **WpdService::DispatchMessage** method examines the **fmtid** field of all incoming commands. If this field is set to WPD\_CATEGORY\_SERVICE\_CAPABILITIES, it forwards the command to the **WpdServiceCapabilities::DispatchWpdMessage** method which, in turn, processes the command. (The **WpdServiceCapabilities::DispatchWpdMessage** method is found in the *WpdServiceCapabilities.cpp* file.)

The following table describes the 14 capability commands that are supported by the **WpdServiceCapabilities::DispatchWpdMessage** method, together with their descriptions and handlers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Description/Handler</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_COMMANDS</td>
<td align="left"><p>Description: Issued when an application calls<strong>IPortableDeviceServiceCapabilities::GetSupportedCommands</strong> to retrieve the list of supported WPD commands for the current service.</p>
<p>Handler: <strong>OnGetSupportedCommands</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_COMMAND_OPTIONS</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetCommandOptions</strong> to retrieve any WPD command options that are implemented by the current service.</p>
<p>Handler: <strong>OnGetCommandOptions</strong></p></td>
</tr>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetSupportedMethods</strong> to retrieve the list of supported device service methods that apply to an object format for the current service.</p>
<p>Handler: <strong>OnGetSupportedMethods</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_METHODS_BY_FORMAT</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetSupportedMethodsByFormat</strong> to retrieve the list of supported device service methods that apply to an object format for the current service.</p>
<p>Handler: <strong>OnGetSupportedMethodsByFormat</strong></p></td>
</tr>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_ATTRIBUTES</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetMethodAttributes</strong> to retrieve the attributes (for example, name and parameters) of a device service method.</p>
<p>Handler: <strong>OnGetMethodAttributes</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_METHOD_PARAMETER_ATTRIBUTES</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetMethodParameterAttributes</strong> to retrieve the parameter attributes (for example, name and VARTYPE) for a given device service method.</p>
<p>Handler: <strong>OnGetMethodParameterAttributes</strong></p></td>
</tr>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMATS</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetSupportedFormats</strong> to retrieve the supported object formats for the current service.</p>
<p>Handler: <strong>OnGetSupportedFormats</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_ATTRIBUTES</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetFormatAttributes</strong> method.</p>
<p>Handler: <strong>OnGetFormatAttributes</strong></p></td>
</tr>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES</td>
<td align="left"><p>Description: Issued when an application calls the <strong>IPortableDeviceServiceCapabilities::GetSupportedFormatProperties</strong> to retrieve the list of supported properties for a given format.</p>
<p>Handler: <strong>OnGetSupportedFormatProperties</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_FORMAT_PROPERTY_ATTRIBUTES</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetFormatPropertyAttributes</strong> to retrieve the attributes (for example, name, form, VARTYPE) of a property.</p>
<p>Handler: <strong>OnGetFormatPropertyAttributes</strong></p></td>
</tr>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_SUPPORTED_EVENTS</td>
<td align="left"><p>Description: Issued when an application call <strong>IPortableDeviceServiceCapabilities::GetSupportedEvents</strong> to retrieve the list of supported events for the current service.</p>
<p>Handler: <strong>OnGetSupportedEvents</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_ATTRIBUTES</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetEventAttributes</strong> to retrieve the attributes (for example, name, parameters) of a device service event.</p>
<p>Handler: <strong>OnGetEventAttributes</strong></p></td>
</tr>
<tr class="odd">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_EVENT_PARAMETER_ATTRIBUTES</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetEventParameterAttributes</strong> to retrieve the attributes of a given event parameter.</p>
<p>Handler: <strong>OnGetEventParameterAttributes</strong></p></td>
</tr>
<tr class="even">
<td align="left">WPD_COMMAND_SERVICE_CAPABILITIES_GET_INHERITED_SERVICES</td>
<td align="left"><p>Description: Issued when an application calls <strong>IPortableDeviceServiceCapabilities::GetInheritedServices</strong> to get the abstract services implemented by the current service.</p>
<p>Handler: <strong>OnGetInheritedServices</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="Supporting_the_WPD_COMMAND_SERVICE_METHODS_START_INVOKE_Command"></span><span id="supporting_the_wpd_command_service_methods_start_invoke_command"></span><span id="SUPPORTING_THE_WPD_COMMAND_SERVICE_METHODS_START_INVOKE_COMMAND"></span>Supporting the WPD\_COMMAND\_SERVICE\_METHODS\_START\_INVOKE Command


A WPD application invokes the methods that are supported by a given service by calling one of two methods that are found in the **IPortableDeviceServiceMethods** interface. The **IPortableDeviceServiceMethods::Invoke** method invokes a method synchronously while the **IPortableDeviceServiceMethods::InvokeAsync** method invokes a given method asynchronously.

When an application calls either of these two methods, the WPD API, in turn, issues the WPD\_COMMAND\_SERVICE\_METHODS\_START\_INVOKE command to the driver.

In the sample driver, the WPD\_COMMAND\_SERVICE\_METHODS\_START\_INVOKE command results in calls to the methods in the following table, which are found in the *WpdServiceMethods.cpp* module.

| Method name                          | Description                                                                                                                                                                                                           |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WpdServiceMethods::OnStartInvoke** | Calls the **StartMethod** helper function and upon completion, returns the invoked method's context in an **IPortableDeviceValues** object.                                                                           |
| **WpdServiceMethods::StartMethod**   | Verifies that the given service supports the requested method, and if it does, creates a new **ServiceMethodContext** object. After the context is created, the **ServiceMethodContext::Initalize** method is called. |
| **ServiceMethodContext::Initialize** | Creates a **CMethodTask** object and invokes the **CMethodTask::Run** method.                                                                                                                                         |
| **CMethodTask::Run**                 | Creates a separate thread in which the invoked method can run.                                                                                                                                                        |

 

When the **WpdServiceMethods::OnStartInvoke** method is called, WPD passes a GUID identifier for the method being invoked. This GUID is passed in the data to which the *pParams* argument points.

The GUIDs for supported methods are found in the *ContactDeviceService.h* and *FullEnumSyncDeviceService.h* header files.

The method context is a string that the driver and WPD use to identify and target a given method's invocation. For example, WPD uses this string when it issues the command to cancel a specific invocation of a given method or to signal the completion of that method.

## <span id="Supporting_the_WPD_COMMAND_SERVICE_METHODS_END_INVOKE_Command"></span><span id="supporting_the_wpd_command_service_methods_end_invoke_command"></span><span id="SUPPORTING_THE_WPD_COMMAND_SERVICE_METHODS_END_INVOKE_COMMAND"></span>Supporting the WPD\_COMMAND\_SERVICE\_METHODS\_END\_INVOKE Command


When a method completes, the driver sends a WPD\_EVENT\_SERVICE\_COMPLETE event to the WPD API. The event data includes the method context that the driver created when it invoked that method. Upon receiving this event notification, the WPD API issues the WPD\_COMMAND\_SERVICE\_METHODS\_END\_INVOKE command and includes the method context with this command. When the sample driver receives this command, it results in calls to the following methods that are found in *WpdServiceMethods.cpp*.

| Method name                        | Description                                                                                                                                                                                                                   |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WpdServiceMethods::OnEndInvoke** | Calls the **EndMethod** helper function and upon completion, returns the invoked method's results and status code. This method also performs any necessary clean up of resources that are associated with the method context. |
| **WpdServiceMethods::EndMethod**   | Retrieves the invoked method's results and status code..                                                                                                                                                                      |

 

## <span id="related_topics"></span>Related topics


****
[The WpdServiceSampleDriver](the-wpdservicesampledriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





