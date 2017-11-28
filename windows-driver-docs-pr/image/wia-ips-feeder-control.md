---
title: WIA\_IPS\_FEEDER\_CONTROL
description: The WIA\_IPS\_FEEDER\_CONTROL property is used to configure manual control over the feeder motor. The WIA minidriver creates and maintains this property.
ms.assetid: CA19D573-B461-4D3E-BE2A-CF350E0FA4EA
keywords: ["WIA_IPS_FEEDER_CONTROL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_FEEDER_CONTROL
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_FEEDER\_CONTROL


The **WIA\_IPS\_FEEDER\_CONTROL** property is used to configure manual control over the feeder motor. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_FEEDER\_CONTROL** property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_FEEDER_CONTROL_AUTO</p></td>
<td><p>The device controls the feeder motor operation. The feeder is started and stopped for each scan job ([<strong>IWiaMiniDrv::drvAcquireItemData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543956) call). This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_FEEDER_CONTROL_MANUAL</p></td>
<td><p>The application controls the feeder motor operation. The feeder is started when the WIA minidriver receives a WIA_COMMAND_START_FEEDER command request and stopped when the WIA minidriver receives a WIA_COMMAND_STOP_FEEDER command request.</p></td>
</tr>
</tbody>
</table>

 

When the device supports this feature, the WIA application can use it to start the feeder motor before executing the first scan job (the first **IWiaTransfer::Download** call) and stop the feeder after the last scan job (the last **IWiaTransfer::Download** call in the current WIA application session) is complete. Between the individual jobs (**IWiaTransfer::Download** calls), the feeder is kept to its operating speed and is ready to continue the next job without delay.

If the WIA minidriver receives an [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) request while WIA\_FEEDER\_CONTROL\_MANUAL is set and without receiving a WIA\_COMMAND\_START\_FEEDER command, the WIA minidriver must revert to WIA\_FEEDER\_COMMAND\_AUTO before executing the scan job.

If WIA\_FEEDER\_CONTROL\_MANUAL is set and the WIA minidriver receives a [**IWiaMiniDrv::drvUnInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff545010) request without receiving a WIA\_COMMAND\_STOP\_FEEDER command, the WIA minidriver must stop the feeder before returning to the call.

This property is valid only for the Feeder item (WIA\_CATEGORY\_FEEDER) and is optional.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_FEEDER_CONTROL%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




