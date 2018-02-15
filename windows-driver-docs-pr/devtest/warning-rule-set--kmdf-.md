---
title: Warning rule set (KMDF)
description: Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.
ms.assetid: 0C012253-9FBD-4B5C-9A93-AF72405EF3E4
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
<td align="left"><p>[<strong>DeferredRequestCompleted</strong>](kmdf-deferredrequestcompleted.md)</p></td>
<td align="left"><p>The [<strong>DeferredRequestCompleted</strong>](kmdf-deferredrequestcompleted.md) rule specifies that if an I/O request presented to a driver's default I/O queue is not completed in the callback function but is deferred for later processing, the request must be completed in a deferred processing callback function, unless the request is forwarded and delivered to the framework, or unless the [<strong>WdfRequestStopAcknowledge</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550033) method is called.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DriverAttributeChanged</strong>](kmdf-driverattributechanged.md)</p></td>
<td align="left"><p>The [<strong>DriverAttributeChanged</strong>](kmdf-driverattributechanged.md) rule specifies that a driver must not change the execution level or synchronization scope of a KMDF driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvAckIoStop</strong>](kmdf-drvackiostop.md)</p></td>
<td align="left"><p>The [<strong>DrvAckIoStop</strong>](kmdf-drvackiostop.md) rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly. In the case of self-managed I/O requests, the driver should also correctly handle these requests from its [<em>EvtDeviceSelfManagedIoSuspend</em>](https://msdn.microsoft.com/library/windows/hardware/ff540907) function. A driver that fails to handle these requests during a power-down would cause [<strong>Bug Check 0x9F: DRIVER_POWER_STATE_FAILURE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559329).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EvtIoResumeGetParam</strong>](kmdf-evtioresumegetparam.md)</p></td>
<td align="left"><p>The [<strong>EvtIoResumeGetParam</strong>](kmdf-evtioresumegetparam.md) rule specifies that [<strong>WdfRequestGetParameters</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549969) is not called within the <strong>EvtIoResumeGetParam</strong> callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EvtIoStopGetParam</strong>](kmdf-evtiostopgetparam.md)</p></td>
<td align="left"><p>The [<strong>EvtIoStopGetParam</strong>](kmdf-evtiostopgetparam.md) rule checks that [<strong>WdfRequestGetParameters</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549969) is not called within [<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EvtIoStopResume</strong>](kmdf-evtiostopresume.md)</p></td>
<td align="left"><p>The [<strong>EvtIoStopResume</strong>](kmdf-evtiostopresume.md) rule specifies that if a driver registers a [<em>EvtIoStop</em>](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback function and then calls [<strong>WdfRequestStopAcknowledge</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550033) with the <em>Requeue</em> parameter equal to <strong>FALSE</strong>, the driver must register a [<em>EvtIoResume</em>](https://msdn.microsoft.com/library/windows/hardware/ff541779) callback function. The framework delivers requests to the <strong>EvtIoResume</strong> callback function when the device enters the D0 state again.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EvtSurpriseRemoveNoRequestComplete</strong>](kmdf-evtsurpriseremovenorequestcomplete.md)</p></td>
<td align="left"><p>The [<strong>EvtSurpriseRemoveNoRequestComplete</strong>](kmdf-evtsurpriseremovenorequestcomplete.md) rule specifies that WDF drivers shouldn’t complete requests from [<em>EvtDeviceSurpriseRemoval</em>](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback, instead self-managed I/O callback functions should be used. <em>EvtDeviceSurpriseRemoval</em> callback isn’t synchronized with the power-down path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FDOPowerPolicyOwnerAPI</strong>](kmdf-fdopowerpolicyownerapi.md)</p></td>
<td align="left"><p>The [<strong>FDOPowerPolicyOwnerAPI</strong>](kmdf-fdopowerpolicyownerapi.md) rule specifies that if an FDO driver relinquishes power policy ownership, the methods [<strong>WdfDeviceInitSetPowerPolicyEventCallbacks</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546774), [<strong>WdfDeviceAssignS0IdleSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545903), and [<strong>WdfDeviceAssignSxWakeSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545909) can only be called on the execution paths where the driver is a power policy owner. SDV issues a warning for this rule.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NoCancelFromEvtSurpriseRemove</strong>](kmdf-nocancelfromevtsurpriseremove.md)</p></td>
<td align="left"><p>The [<strong>NoCancelFromEvtSurpriseRemove</strong>](kmdf-nocancelfromevtsurpriseremove.md) rule specifies that WDF Drivers shouldn’t cancel requests from the [<em>EvtDeviceSurpriseRemoval</em>](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function, instead self-managed I/O callback functions should be used. <em>EvtDeviceSurpriseRemoval</em> callback function isn’t synchronized with the power-down path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PagedCodeAtD0</strong>](kmdf-pagedcodeatd0.md)</p></td>
<td align="left"><p>The [<strong>PagedCodeAtD0</strong>](kmdf-pagedcodeatd0.md) rule specifies that a driver must not mark code as pageable within callback functions that are in the power-up code path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ParentObjectCheck</strong>](kmdf-parentobjectcheck.md)</p></td>
<td align="left"><p>The [<strong>ParentObjectCheck</strong>](kmdf-parentobjectcheck.md) rule specifies that driver should call [<strong>WdfMemoryCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548706) specifying a parent object using a [<strong>WDF_OBJECT_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. If driver doesn’t set a parent object for the framework memory object then the framework sets the driver as the default parent, so that unless the driver deletes the framework memory object explicitly it’ll remain in the memory until the driver object unloads.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ReqNotCanceledLocal</strong>](kmdf-reqnotcanceledlocal.md)</p></td>
<td align="left"><p>The [<strong>ReqNotCanceledLocal</strong>](kmdf-reqnotcanceledlocal.md) rule specifies that if a request marked as cancelable is completed in a default I/O queue callback function, the [<strong>WdfRequestUnmarkCancelable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550035) method must be called on the I/O request before completion. The I/O request must be completed, unless the request is canceled before it calls <strong>WdfRequestUnmarkCancelable</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ReqSendFail</strong>](kmdf-reqsendfail.md)</p></td>
<td align="left"><p>The [<strong>ReqSendFail</strong>](kmdf-reqsendfail.md) rule specifies that a driver must set the correct completion status in cases in which the [<strong>WdfRequestSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550027) method might fail.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RequestCompletedLocal</strong>](kmdf-requestcompletedlocal.md)</p></td>
<td align="left"><p>The [<strong>RequestCompletedLocal</strong>](kmdf-requestcompletedlocal.md) rule specifies that if an I/O request is not completed in any of the [<em>EvtIoDefault</em>](https://msdn.microsoft.com/library/windows/hardware/ff541757), [<em>EvtIoRead</em>](https://msdn.microsoft.com/library/windows/hardware/ff541776), [<em>EvtIoWrite</em>](https://msdn.microsoft.com/library/windows/hardware/ff541813), [<em>EvtIoDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541758), and [<em>EvtIoInternalDeviceControl</em>](https://msdn.microsoft.com/library/windows/hardware/ff541768) callback functions, and if [<strong>WdfRequestMarkCancelable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549983) was not called on the request within the callback function, there might be a problem with request completion in the driver's code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RequestForUrbXrb</strong>](kmdf-requestforurbxrb.md)</p></td>
<td align="left"><p>If the client driver calls [<strong>WdfUsbTargetDeviceCreateWithParameters</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439428) and specifies the client contract version USBD_CLIENT_CONTRACT_VERSION_602 in the WDF_USB_DEVICE_CREATE_CONFIG structure (to use the new capabilities of the USB driver stack for Windows 8), DDIs that use a URB internally would only use <em>URB context</em> if any of the following preconditions apply:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SyncReqSend</strong>](kmdf-syncreqsend.md)</p></td>
<td align="left"><p>The [<strong>SyncReqSend</strong>](kmdf-syncreqsend.md) rule specifies that all synchronous send requests are done by using synchronous-specific KMDF device driver interface methods, and that the methods have a nonzero timeout value set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SyncReqSend2</strong>](kmdf-syncreqsend2.md)</p></td>
<td align="left"><p>The [<strong>SyncReqSend2</strong>](kmdf-syncreqsend2.md) rule specifies that synchronous request sends have a nonzero time-out value set.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Warning%20rule%20set%20%28KMDF%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




