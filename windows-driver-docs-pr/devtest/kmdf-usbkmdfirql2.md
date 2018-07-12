---
title: UsbKmdfIrql2 rule (kmdf)
description: The UsbKmdfIrql2 rule specifies that a KMDF driver should not call USB-specific DDIs at the incorrect IRQL level.
ms.assetid: D514B902-8F29-4D77-A26F-57DA43A045E8
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["UsbKmdfIrql2 rule (kmdf)"]
topic_type:
- apiref
api_name:
- UsbKmdfIrql2
api_type:
- NA
---

# UsbKmdfIrql2 rule (kmdf)


The **UsbKmdfIrql2** rule specifies that a KMDF driver should not call USB-specific DDIs at the incorrect IRQL level.

|              |      |
|--------------|------|
| Driver model | KMDF |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>UsbKmdfIrql2</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfUsbInterfaceGetConfiguredPipe**](https://msdn.microsoft.com/library/windows/hardware/ff550057)
[**WdfUsbInterfaceGetConfiguredSettingIndex**](https://msdn.microsoft.com/library/windows/hardware/ff550059)
[**WdfUsbInterfaceGetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550060)
[**WdfUsbInterfaceGetEndpointInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550063)
[**WdfUsbInterfaceGetInterfaceNumber**](https://msdn.microsoft.com/library/windows/hardware/ff550065)
[**WdfUsbInterfaceGetNumConfiguredPipes**](https://msdn.microsoft.com/library/windows/hardware/ff550066)
[**WdfUsbInterfaceGetNumEndpoints**](https://msdn.microsoft.com/library/windows/hardware/ff550068)
[**WdfUsbInterfaceGetNumSettings**](https://msdn.microsoft.com/library/windows/hardware/ff550070)
[**WdfUsbInterfaceSelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff550073)
[**WdfUsbTargetDeviceAllocAndQueryString**](https://msdn.microsoft.com/library/windows/hardware/ff550074)
[**WdfUsbTargetDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550077)
[**WdfUsbTargetDeviceCyclePortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550080)
[**WdfUsbTargetDeviceFormatRequestForControlTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff550082)
[**WdfUsbTargetDeviceFormatRequestForCyclePort**](https://msdn.microsoft.com/library/windows/hardware/ff550084)
[**WdfUsbTargetDeviceFormatRequestForString**](https://msdn.microsoft.com/library/windows/hardware/ff550086)
[**WdfUsbTargetDeviceFormatRequestForUrb**](https://msdn.microsoft.com/library/windows/hardware/ff550088)
[**WdfUsbTargetDeviceGetDeviceDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550090)
[**WdfUsbTargetDeviceGetInterface**](https://msdn.microsoft.com/library/windows/hardware/ff550092)
[**WdfUsbTargetDeviceGetNumInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff550094)
[**WdfUsbTargetDeviceIsConnectedSynchronous**](https://msdn.microsoft.com/library/windows/hardware/ff550095)
[**WdfUsbTargetDeviceQueryString**](https://msdn.microsoft.com/library/windows/hardware/ff550096)
[**WdfUsbTargetDeviceResetPortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550097)
[**WdfUsbTargetDeviceRetrieveConfigDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550098)
[**WdfUsbTargetDeviceRetrieveCurrentFrameNumber**](https://msdn.microsoft.com/library/windows/hardware/ff550099)
[**WdfUsbTargetDeviceRetrieveInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550100)
[**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101)
[**WdfUsbTargetDeviceSendControlTransferSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550104)
[**WdfUsbTargetDeviceSendUrbSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550105)
[**WdfUsbTargetDeviceWdmGetConfigurationHandle**](https://msdn.microsoft.com/library/windows/hardware/ff551127)
[**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129)
[**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130)
[**WdfUsbTargetPipeFormatRequestForAbort**](https://msdn.microsoft.com/library/windows/hardware/ff551132)
[**WdfUsbTargetPipeFormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff551136)
[**WdfUsbTargetPipeFormatRequestForReset**](https://msdn.microsoft.com/library/windows/hardware/ff551138)
[**WdfUsbTargetPipeFormatRequestForUrb**](https://msdn.microsoft.com/library/windows/hardware/ff551139)
[**WdfUsbTargetPipeFormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff551141)
[**WdfUsbTargetPipeGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff551142)
[**WdfUsbTargetPipeGetType**](https://msdn.microsoft.com/library/windows/hardware/ff551148)
[**WdfUsbTargetPipeIsInEndpoint**](https://msdn.microsoft.com/library/windows/hardware/ff551151)
[**WdfUsbTargetPipeIsOutEndpoint**](https://msdn.microsoft.com/library/windows/hardware/ff551153)
[**WdfUsbTargetPipeReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551155)
[**WdfUsbTargetPipeResetSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551156)
[**WdfUsbTargetPipeSendUrbSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551158)
[**WdfUsbTargetPipeSetNoMaximumPacketSizeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff551160)
[**WdfUsbTargetPipeWdmGetPipeHandle**](https://msdn.microsoft.com/library/windows/hardware/ff551162)
[**WdfUsbTargetPipeWriteSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551163)
 

 





