---
title: DeviceInitAPI rule (kmdf)
description: For an FDO device, the framework device object initialization methods and the framework FDO initialization methods must be called before the driver calls the WdfDeviceCreate method for the device object.
ms.date: 05/21/2018
keywords: ["DeviceInitAPI rule (kmdf)"]
topic_type:
- apiref
api_name:
- DeviceInitAPI
api_type:
- NA
ms.localizationpriority: medium
---

# DeviceInitAPI rule (kmdf)


For an FDO device, the framework device object initialization methods and the framework FDO initialization methods must be called before the driver calls the [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) method for the device object.

For an FDO device, the framework device object initialization methods and framework FDO initialization methods, which store information in the [WDFDEVICE\_INIT](../wdf/wdfdevice_init.md) structure, cannot be called after the driver calls [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) for the framework device object.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>DeviceInitAPI</strong> rule.</p>
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

[**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate)  
[**WdfDeviceInitAssignName**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignname)  
[**WdfDeviceInitAssignSDDLString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignsddlstring)  
[**WdfDeviceInitAssignWdmIrpPreprocessCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback)  
[**WdfDeviceInitRegisterPnpStateChangeCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpnpstatechangecallback)  
[**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpowerpolicystatechangecallback)  
[**WdfDeviceInitRegisterPowerStateChangeCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitregisterpowerstatechangecallback)  
[**WdfDeviceInitSetCharacteristics**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetcharacteristics)  
[**WdfDeviceInitSetDeviceClass**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetdeviceclass)  
[**WdfDeviceInitSetDeviceType**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetdevicetype)  
[**WdfDeviceInitSetExclusive**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetexclusive)  
[**WdfDeviceInitSetFileObjectConfig**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetfileobjectconfig)  
[**WdfDeviceInitSetIoInCallerContextCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetioincallercontextcallback)  
[**WdfDeviceInitSetIoType**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotype)  
[**WdfDeviceInitSetPnpPowerEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks)  
[**WdfDeviceInitSetPowerInrush**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerinrush)  
[**WdfDeviceInitSetPowerNotPageable**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowernotpageable)  
[**WdfDeviceInitSetPowerPageable**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpageable)  
[**WdfDeviceInitSetPowerPolicyEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks)  
[**WdfDeviceInitSetPowerPolicyOwnership**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyownership)  
[**WdfDeviceInitSetRequestAttributes**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetrequestattributes)  
[**WdfFdoInitAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandqueryproperty)  
[**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey)  
[**WdfFdoInitQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitqueryproperty)  
[**WdfFdoInitSetDefaultChildListConfig**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitsetdefaultchildlistconfig)  
[**WdfFdoInitSetEventCallbacks**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitseteventcallbacks)  
[**WdfFdoInitSetFilter**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitsetfilter)  
[**WdfFdoInitWdmGetPhysicalDevice**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitwdmgetphysicaldevice)  
