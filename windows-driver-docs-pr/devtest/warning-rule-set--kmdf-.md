---
title: Warning rule set (KMDF)
description: Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.
ms.assetid: 0C012253-9FBD-4B5C-9A93-AF72405EF3E4
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Warning rule set (KMDF)


Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="kmdf-deferredrequestcompleted.md" data-raw-source="[&lt;strong&gt;DeferredRequestCompleted&lt;/strong&gt;](kmdf-deferredrequestcompleted.md)"><strong>DeferredRequestCompleted</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-deferredrequestcompleted.md" data-raw-source="[&lt;strong&gt;DeferredRequestCompleted&lt;/strong&gt;](kmdf-deferredrequestcompleted.md)"><strong>DeferredRequestCompleted</strong></a> rule specifies that if an I/O request presented to a driver&#39;s default I/O queue is not completed in the callback function but is deferred for later processing, the request must be completed in a deferred processing callback function, unless the request is forwarded and delivered to the framework, or unless the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550033" data-raw-source="[&lt;strong&gt;WdfRequestStopAcknowledge&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550033)"><strong>WdfRequestStopAcknowledge</strong></a> method is called.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-driverattributechanged.md" data-raw-source="[&lt;strong&gt;DriverAttributeChanged&lt;/strong&gt;](kmdf-driverattributechanged.md)"><strong>DriverAttributeChanged</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-driverattributechanged.md" data-raw-source="[&lt;strong&gt;DriverAttributeChanged&lt;/strong&gt;](kmdf-driverattributechanged.md)"><strong>DriverAttributeChanged</strong></a> rule specifies that a driver must not change the execution level or synchronization scope of a KMDF driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-drvackiostop.md" data-raw-source="[&lt;strong&gt;DrvAckIoStop&lt;/strong&gt;](kmdf-drvackiostop.md)"><strong>DrvAckIoStop</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-drvackiostop.md" data-raw-source="[&lt;strong&gt;DrvAckIoStop&lt;/strong&gt;](kmdf-drvackiostop.md)"><strong>DrvAckIoStop</strong></a> rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly. In the case of self-managed I/O requests, the driver should also correctly handle these requests from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540907" data-raw-source="[&lt;em&gt;EvtDeviceSelfManagedIoSuspend&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540907)"><em>EvtDeviceSelfManagedIoSuspend</em></a> function. A driver that fails to handle these requests during a power-down would cause <a href="https://msdn.microsoft.com/library/windows/hardware/ff559329" data-raw-source="[&lt;strong&gt;Bug Check 0x9F: DRIVER_POWER_STATE_FAILURE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559329)"><strong>Bug Check 0x9F: DRIVER_POWER_STATE_FAILURE</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-evtioresumegetparam.md" data-raw-source="[&lt;strong&gt;EvtIoResumeGetParam&lt;/strong&gt;](kmdf-evtioresumegetparam.md)"><strong>EvtIoResumeGetParam</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-evtioresumegetparam.md" data-raw-source="[&lt;strong&gt;EvtIoResumeGetParam&lt;/strong&gt;](kmdf-evtioresumegetparam.md)"><strong>EvtIoResumeGetParam</strong></a> rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff549969" data-raw-source="[&lt;strong&gt;WdfRequestGetParameters&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549969)"><strong>WdfRequestGetParameters</strong></a> is not called within the <strong>EvtIoResumeGetParam</strong> callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-evtiostopgetparam.md" data-raw-source="[&lt;strong&gt;EvtIoStopGetParam&lt;/strong&gt;](kmdf-evtiostopgetparam.md)"><strong>EvtIoStopGetParam</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-evtiostopgetparam.md" data-raw-source="[&lt;strong&gt;EvtIoStopGetParam&lt;/strong&gt;](kmdf-evtiostopgetparam.md)"><strong>EvtIoStopGetParam</strong></a> rule checks that <a href="https://msdn.microsoft.com/library/windows/hardware/ff549969" data-raw-source="[&lt;strong&gt;WdfRequestGetParameters&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549969)"><strong>WdfRequestGetParameters</strong></a> is not called within <a href="https://msdn.microsoft.com/library/windows/hardware/ff541788" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541788)"><em>EvtIoStop</em></a> callback.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-evtiostopresume.md" data-raw-source="[&lt;strong&gt;EvtIoStopResume&lt;/strong&gt;](kmdf-evtiostopresume.md)"><strong>EvtIoStopResume</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-evtiostopresume.md" data-raw-source="[&lt;strong&gt;EvtIoStopResume&lt;/strong&gt;](kmdf-evtiostopresume.md)"><strong>EvtIoStopResume</strong></a> rule specifies that if a driver registers a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541788" data-raw-source="[&lt;em&gt;EvtIoStop&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541788)"><em>EvtIoStop</em></a> callback function and then calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550033" data-raw-source="[&lt;strong&gt;WdfRequestStopAcknowledge&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550033)"><strong>WdfRequestStopAcknowledge</strong></a> with the <em>Requeue</em> parameter equal to <strong>FALSE</strong>, the driver must register a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541779" data-raw-source="[&lt;em&gt;EvtIoResume&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541779)"><em>EvtIoResume</em></a> callback function. The framework delivers requests to the <strong>EvtIoResume</strong> callback function when the device enters the D0 state again.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-evtsurpriseremovenorequestcomplete.md" data-raw-source="[&lt;strong&gt;EvtSurpriseRemoveNoRequestComplete&lt;/strong&gt;](kmdf-evtsurpriseremovenorequestcomplete.md)"><strong>EvtSurpriseRemoveNoRequestComplete</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-evtsurpriseremovenorequestcomplete.md" data-raw-source="[&lt;strong&gt;EvtSurpriseRemoveNoRequestComplete&lt;/strong&gt;](kmdf-evtsurpriseremovenorequestcomplete.md)"><strong>EvtSurpriseRemoveNoRequestComplete</strong></a> rule specifies that WDF drivers shouldn’t complete requests from <a href="https://msdn.microsoft.com/library/windows/hardware/ff540913" data-raw-source="[&lt;em&gt;EvtDeviceSurpriseRemoval&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540913)"><em>EvtDeviceSurpriseRemoval</em></a> callback, instead self-managed I/O callback functions should be used. <em>EvtDeviceSurpriseRemoval</em> callback isn’t synchronized with the power-down path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-fdopowerpolicyownerapi.md" data-raw-source="[&lt;strong&gt;FDOPowerPolicyOwnerAPI&lt;/strong&gt;](kmdf-fdopowerpolicyownerapi.md)"><strong>FDOPowerPolicyOwnerAPI</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-fdopowerpolicyownerapi.md" data-raw-source="[&lt;strong&gt;FDOPowerPolicyOwnerAPI&lt;/strong&gt;](kmdf-fdopowerpolicyownerapi.md)"><strong>FDOPowerPolicyOwnerAPI</strong></a> rule specifies that if an FDO driver relinquishes power policy ownership, the methods <a href="https://msdn.microsoft.com/library/windows/hardware/ff546774" data-raw-source="[&lt;strong&gt;WdfDeviceInitSetPowerPolicyEventCallbacks&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546774)"><strong>WdfDeviceInitSetPowerPolicyEventCallbacks</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903" data-raw-source="[&lt;strong&gt;WdfDeviceAssignS0IdleSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545903)"><strong>WdfDeviceAssignS0IdleSettings</strong></a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545909" data-raw-source="[&lt;strong&gt;WdfDeviceAssignSxWakeSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545909)"><strong>WdfDeviceAssignSxWakeSettings</strong></a> can only be called on the execution paths where the driver is a power policy owner. SDV issues a warning for this rule.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-nocancelfromevtsurpriseremove.md" data-raw-source="[&lt;strong&gt;NoCancelFromEvtSurpriseRemove&lt;/strong&gt;](kmdf-nocancelfromevtsurpriseremove.md)"><strong>NoCancelFromEvtSurpriseRemove</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-nocancelfromevtsurpriseremove.md" data-raw-source="[&lt;strong&gt;NoCancelFromEvtSurpriseRemove&lt;/strong&gt;](kmdf-nocancelfromevtsurpriseremove.md)"><strong>NoCancelFromEvtSurpriseRemove</strong></a> rule specifies that WDF Drivers shouldn’t cancel requests from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540913" data-raw-source="[&lt;em&gt;EvtDeviceSurpriseRemoval&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540913)"><em>EvtDeviceSurpriseRemoval</em></a> callback function, instead self-managed I/O callback functions should be used. <em>EvtDeviceSurpriseRemoval</em> callback function isn’t synchronized with the power-down path.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-pagedcodeatd0.md" data-raw-source="[&lt;strong&gt;PagedCodeAtD0&lt;/strong&gt;](kmdf-pagedcodeatd0.md)"><strong>PagedCodeAtD0</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-pagedcodeatd0.md" data-raw-source="[&lt;strong&gt;PagedCodeAtD0&lt;/strong&gt;](kmdf-pagedcodeatd0.md)"><strong>PagedCodeAtD0</strong></a> rule specifies that a driver must not mark code as pageable within callback functions that are in the power-up code path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-parentobjectcheck.md" data-raw-source="[&lt;strong&gt;ParentObjectCheck&lt;/strong&gt;](kmdf-parentobjectcheck.md)"><strong>ParentObjectCheck</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-parentobjectcheck.md" data-raw-source="[&lt;strong&gt;ParentObjectCheck&lt;/strong&gt;](kmdf-parentobjectcheck.md)"><strong>ParentObjectCheck</strong></a> rule specifies that driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548706" data-raw-source="[&lt;strong&gt;WdfMemoryCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548706)"><strong>WdfMemoryCreate</strong></a> specifying a parent object using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400" data-raw-source="[&lt;strong&gt;WDF_OBJECT_ATTRIBUTES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552400)"><strong>WDF_OBJECT_ATTRIBUTES</strong></a> structure. If driver doesn’t set a parent object for the framework memory object then the framework sets the driver as the default parent, so that unless the driver deletes the framework memory object explicitly it’ll remain in the memory until the driver object unloads.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-reqnotcanceledlocal.md" data-raw-source="[&lt;strong&gt;ReqNotCanceledLocal&lt;/strong&gt;](kmdf-reqnotcanceledlocal.md)"><strong>ReqNotCanceledLocal</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-reqnotcanceledlocal.md" data-raw-source="[&lt;strong&gt;ReqNotCanceledLocal&lt;/strong&gt;](kmdf-reqnotcanceledlocal.md)"><strong>ReqNotCanceledLocal</strong></a> rule specifies that if a request marked as cancelable is completed in a default I/O queue callback function, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550035" data-raw-source="[&lt;strong&gt;WdfRequestUnmarkCancelable&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550035)"><strong>WdfRequestUnmarkCancelable</strong></a> method must be called on the I/O request before completion. The I/O request must be completed, unless the request is canceled before it calls <strong>WdfRequestUnmarkCancelable</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-reqsendfail.md" data-raw-source="[&lt;strong&gt;ReqSendFail&lt;/strong&gt;](kmdf-reqsendfail.md)"><strong>ReqSendFail</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-reqsendfail.md" data-raw-source="[&lt;strong&gt;ReqSendFail&lt;/strong&gt;](kmdf-reqsendfail.md)"><strong>ReqSendFail</strong></a> rule specifies that a driver must set the correct completion status in cases in which the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550027)"><strong>WdfRequestSend</strong></a> method might fail.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-requestcompletedlocal.md" data-raw-source="[&lt;strong&gt;RequestCompletedLocal&lt;/strong&gt;](kmdf-requestcompletedlocal.md)"><strong>RequestCompletedLocal</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-requestcompletedlocal.md" data-raw-source="[&lt;strong&gt;RequestCompletedLocal&lt;/strong&gt;](kmdf-requestcompletedlocal.md)"><strong>RequestCompletedLocal</strong></a> rule specifies that if an I/O request is not completed in any of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541757" data-raw-source="[&lt;em&gt;EvtIoDefault&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541757)"><em>EvtIoDefault</em></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541776" data-raw-source="[&lt;em&gt;EvtIoRead&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541776)"><em>EvtIoRead</em></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541813" data-raw-source="[&lt;em&gt;EvtIoWrite&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541813)"><em>EvtIoWrite</em></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff541758" data-raw-source="[&lt;em&gt;EvtIoDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541758)"><em>EvtIoDeviceControl</em></a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff541768" data-raw-source="[&lt;em&gt;EvtIoInternalDeviceControl&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541768)"><em>EvtIoInternalDeviceControl</em></a> callback functions, and if <a href="https://msdn.microsoft.com/library/windows/hardware/ff549983" data-raw-source="[&lt;strong&gt;WdfRequestMarkCancelable&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549983)"><strong>WdfRequestMarkCancelable</strong></a> was not called on the request within the callback function, there might be a problem with request completion in the driver&#39;s code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-requestforurbxrb.md" data-raw-source="[&lt;strong&gt;RequestForUrbXrb&lt;/strong&gt;](kmdf-requestforurbxrb.md)"><strong>RequestForUrbXrb</strong></a></p></td>
<td align="left"><p>If the client driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateWithParameters&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439428)"><strong>WdfUsbTargetDeviceCreateWithParameters</strong></a> and specifies the client contract version USBD_CLIENT_CONTRACT_VERSION_602 in the WDF_USB_DEVICE_CREATE_CONFIG structure (to use the new capabilities of the USB driver stack for Windows 8), DDIs that use a URB internally would only use <em>URB context</em> if any of the following preconditions apply:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-syncreqsend.md" data-raw-source="[&lt;strong&gt;SyncReqSend&lt;/strong&gt;](kmdf-syncreqsend.md)"><strong>SyncReqSend</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-syncreqsend.md" data-raw-source="[&lt;strong&gt;SyncReqSend&lt;/strong&gt;](kmdf-syncreqsend.md)"><strong>SyncReqSend</strong></a> rule specifies that all synchronous send requests are done by using synchronous-specific KMDF device driver interface methods, and that the methods have a nonzero timeout value set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-syncreqsend2.md" data-raw-source="[&lt;strong&gt;SyncReqSend2&lt;/strong&gt;](kmdf-syncreqsend2.md)"><strong>SyncReqSend2</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-syncreqsend2.md" data-raw-source="[&lt;strong&gt;SyncReqSend2&lt;/strong&gt;](kmdf-syncreqsend2.md)"><strong>SyncReqSend2</strong></a> rule specifies that synchronous request sends have a nonzero time-out value set.</p></td>
</tr>
</tbody>
</table>

 

**To select the Warning rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Warning**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Warning.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Warning.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





