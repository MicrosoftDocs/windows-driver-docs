---
title: Modifying SRBs
description: Modifying SRBs
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB modifications WDK storage
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# Modifying SRBs

As mentioned in the preceding section, a SCSI miniport driver's [**DriverEntry**](driverentry-of-scsi-miniport-driver.md) routine must request that the port driver allocate memory for SRB extensions if the miniport driver maintains per-request state information.

Otherwise, a SCSI miniport driver can write values into SRBs *only* for the following purposes and *only* in the following members:

- To return required status about each operation in the **SrbStatus** and **ScsiStatus** members

- If an underrun occurs, to update the **DataTransferLength** member

- If it supports auto request sense and transfers request-sense information, to update the **SenseInfoBufferLength**

- If SRB_FLAGS_UNSPECIFIED_DIRECTION is set in the **SrbFlags** member and the HBA is a subordinate DMA device, to reset the SRB_FLAGS_DATA_IN or SRB_FLAGS_DATA_OUT, as appropriate to the current transfer request

- If the miniport driver supports more than eight logical units, to set the **Lun** member to the logical unit number

If the HBA can handle more than eight logical units, as indicated when *HwScsiFindAdapter* sets up the [PORT_CONFIGURATION_INFORMATION](/windows-hardware/drivers/ddi/srb/ns-srb-_port_configuration_information), the port driver does not interpret LUN information. The miniport driver is responsible for mapping the 8-bit LUN from an SRB to a SCSI-3 address if necessary.

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
