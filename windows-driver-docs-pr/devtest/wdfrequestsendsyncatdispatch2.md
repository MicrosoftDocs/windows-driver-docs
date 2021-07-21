---
title: WdfRequestSendSyncAtDispatch2 rule (kmdf)
description: The WdfRequestSendSyncAtDispatch2 rule verifies that the WdfRequestSend function is sent at the correct IRQL priority level.
ms.date: 05/21/2018
keywords: ["WdfRequestSendSyncAtDispatch2 rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfRequestSendSyncAtDispatch2
api_type:
- NA
ms.localizationpriority: medium
---

# WdfRequestSendSyncAtDispatch2 rule (kmdf)


The **WdfRequestSendSyncAtDispatch2** rule verifies that the [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend) function is sent at the correct IRQL priority level.

If the driver sets the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag, it must call the [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend) function at IRQL = PASSIVE\_LEVEL. If this flag is not set, the driver must call the **WdfRequestSend** function at IRQL = DISPATCH\_LEVEL.

> [!NOTE]
>
> This rule tests the same conditions as the [**WdfRequestSendSyncAtDispatch**](wdfrequestsendsyncatdispatch.md) rule, but it uses a different harness to test different code paths.

 

**Driver model: KMDF**

## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>WdfRequestSendSyncAtDispatch2</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**WdfUsbInterfaceGetConfiguredPipe**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetconfiguredpipe)
[**WdfUsbInterfaceGetConfiguredSettingIndex**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetconfiguredsettingindex)
[**WdfUsbInterfaceGetDescriptor**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetdescriptor)
[**WdfUsbInterfaceGetEndpointInformation**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetendpointinformation)
[**WdfUsbInterfaceGetInterfaceNumber**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetinterfacenumber)
[**WdfUsbInterfaceGetNumConfiguredPipes**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetnumconfiguredpipes)
[**WdfUsbInterfaceGetNumEndpoints**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetnumendpoints)
[**WdfUsbInterfaceGetNumSettings**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetnumsettings)
[**WdfUsbInterfaceSelectSetting**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfaceselectsetting)
[**WdfUsbTargetDeviceAllocAndQueryString**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceallocandquerystring)
[**WdfUsbTargetDeviceCreate**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreate)
[**WdfUsbTargetDeviceCyclePortSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecycleportsynchronously)
[**WdfUsbTargetDeviceFormatRequestForControlTransfer**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)
[**WdfUsbTargetDeviceFormatRequestForCyclePort**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcycleport)
[**WdfUsbTargetDeviceFormatRequestForString**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforstring)
[**WdfUsbTargetDeviceFormatRequestForUrb**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforurb)
[**WdfUsbTargetDeviceGetDeviceDescriptor**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor)
[**WdfUsbTargetDeviceGetInterface**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetinterface)
[**WdfUsbTargetDeviceGetNumInterfaces**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetnuminterfaces)
[**WdfUsbTargetDeviceIsConnectedSynchronous**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceisconnectedsynchronous)
[**WdfUsbTargetDeviceQueryString**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequerystring)
[**WdfUsbTargetDeviceResetPortSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceresetportsynchronously)
[**WdfUsbTargetDeviceRetrieveConfigDescriptor**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)
[**WdfUsbTargetDeviceRetrieveCurrentFrameNumber**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrievecurrentframenumber)
[**WdfUsbTargetDeviceRetrieveInformation**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveinformation)
[**WdfUsbTargetDeviceSelectConfig**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceselectconfig)
[**WdfUsbTargetDeviceSendControlTransferSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)
[**WdfUsbTargetDeviceSendUrbSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)
[**WdfUsbTargetDeviceWdmGetConfigurationHandle**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicewdmgetconfigurationhandle)
[**WdfUsbTargetPipeAbortSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeabortsynchronously)
[**WdfUsbTargetPipeConfigContinuousReader**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeconfigcontinuousreader)
[**WdfUsbTargetPipeFormatRequestForAbort**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforabort)
[**WdfUsbTargetPipeFormatRequestForRead**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforread)
[**WdfUsbTargetPipeFormatRequestForReset**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforreset)
[**WdfUsbTargetPipeFormatRequestForUrb**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforurb)
[**WdfUsbTargetPipeFormatRequestForWrite**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforwrite)
[**WdfUsbTargetPipeGetInformation**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipegetinformation)
[**WdfUsbTargetPipeGetType**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipegettype)
[**WdfUsbTargetPipeIsInEndpoint**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeisinendpoint)
[**WdfUsbTargetPipeIsOutEndpoint**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeisoutendpoint)
[**WdfUsbTargetPipeReadSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipereadsynchronously)
[**WdfUsbTargetPipeResetSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpiperesetsynchronously)
[**WdfUsbTargetPipeSendUrbSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipesendurbsynchronously)
[**WdfUsbTargetPipeSetNoMaximumPacketSizeCheck**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipesetnomaximumpacketsizecheck)
[**WdfUsbTargetPipeWdmGetPipeHandle**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewdmgetpipehandle)
[**WdfUsbTargetPipeWriteSynchronously**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewritesynchronously)
