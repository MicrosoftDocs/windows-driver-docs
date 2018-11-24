---
title: Modifying SRBs
description: Modifying SRBs
ms.assetid: 9077cfab-c17c-4c8e-9740-0895f227fb4b
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB modifications WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying SRBs


## <span id="ddk_modifying_srbs_kg"></span><span id="DDK_MODIFYING_SRBS_KG"></span>


As mentioned in the preceding section, a SCSI miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine must request that the port driver allocate memory for SRB extensions if the miniport driver maintains per-request state information.

Otherwise, a SCSI miniport driver can write values into SRBs *only* for the following purposes and *only* in the following members:

-   To return required status about each operation in the **SrbStatus** and **ScsiStatus** members

-   If an underrun occurs, to update the **DataTransferLength** member

-   If it supports auto request sense and transfers request-sense information, to update the **SenseInfoBufferLength**

-   If SRB\_FLAGS\_UNSPECIFIED\_DIRECTION is set in the **SrbFlags** member and the HBA is a subordinate DMA device, to reset the SRB\_FLAGS\_DATA\_IN or SRB\_FLAGS\_DATA\_OUT, as appropriate to the current transfer request

-   If the miniport driver supports more than eight logical units, to set the **Lun** member to the logical unit number

If the HBA can handle more than eight logical units, as indicated when *HwScsiFindAdapter* sets up the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900), the port driver does not interpret LUN information. The miniport driver is responsible for mapping the 8-bit LUN from an SRB to a SCSI-3 address if necessary.

The mapping from the 8-bit LUN to SCSI-3 address is miniport driver-specific. The following tables show the recommended mapping, where *P* is the physical addressing mode, *B* is the bus, and *T* is the target.

8-bit LUN

<table>
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Bit/Byte</p></td>
<td align="left"><p>7</p></td>
<td align="left"><p>6</p></td>
<td align="left"><p>5</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>3</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>P</p></td>
<td align="left"><p>P</p></td>
<td align="left"><p>B</p></td>
<td align="left"><p>B</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>T</p></td>
</tr>
</tbody>
</table>

 

SCSI-3 Address

<table>
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Bit/Byte</p></td>
<td align="left"><p>7</p></td>
<td align="left"><p>6</p></td>
<td align="left"><p>5</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>3</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>P</p></td>
<td align="left"><p>P</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>B</p></td>
<td align="left"><p>B</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>T</p></td>
</tr>
</tbody>
</table>

 

The SCSI port driver reserves LUN 0xFF to indicate all logical units.

 

 




