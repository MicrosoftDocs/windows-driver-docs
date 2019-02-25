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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_FEEDER\_CONTROL


The **WIA\_IPS\_FEEDER\_CONTROL** property is used to configure manual control over the feeder motor. The WIA minidriver creates and maintains this property.




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
<td><p>The device controls the feeder motor operation. The feeder is started and stopped for each scan job (<a href="https://msdn.microsoft.com/library/windows/hardware/ff543956" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvAcquireItemData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543956)"><strong>IWiaMiniDrv::drvAcquireItemData</strong></a> call). This is the required default value if the property is supported.</p></td>
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

 

 





