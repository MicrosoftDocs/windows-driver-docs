---
title: OID_WWAN_DEVICE_CAPS
description: OID_WWAN_DEVICE_CAPS returns the capabilities of the MB device, including the cellular technology it supports, the classes of packet data it supports, the radio frequencies it supports, the type of voice service it provides, and whether it uses a Subscriber Identity Module (SIM card). The supported cellular technology and whether the device uses a SIM are particularly important because network provider selection and SIM user interfaces depend on the values of these two capabilities. The manufacturer and firmware revision are returned as optional fields. Set requests are not supported. Miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request, and later sending a NDIS_STATUS_WWAN_DEVICE_CAPS status notification containing a NDIS_WWAN_DEVICE_CAPS structure that indicates the capabilities of the MB device when completing query requests.
ms.assetid: bcf04d0b-70f3-48b7-a505-c82e50edadb2
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DEVICE_CAPS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_DEVICE\_CAPS


OID\_WWAN\_DEVICE\_CAPS returns the capabilities of the MB device, including the cellular technology it supports, the classes of packet data it supports, the radio frequencies it supports, the type of voice service it provides, and whether it uses a Subscriber Identity Module (SIM card). The supported cellular technology and whether the device uses a SIM are particularly important because network provider selection and SIM user interfaces depend on the values of these two capabilities. The manufacturer and firmware revision are returned as optional fields.

Set requests are not supported.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567845) status notification containing a [**NDIS\_WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567907) structure that indicates the capabilities of the MB device when completing query requests.

Remarks
-------

Starting with Windows 8, the MB driver model has been updated to version 2.0. Windows 8 miniport drivers should set the **Header.Revision** member of the [**NDIS\_WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567907) structure to **NDIS\_WWAN\_DEVICE\_CAPS\_REVISION\_2** for *query* requests. Windows 7 miniport drivers should set the **Header.Revision** member of the **NDIS\_WWAN\_DEVICE\_CAPS** structure to **NDIS\_WWAN\_DEVICE\_CAPS\_REVISION\_1** for *query* requests.

For more information about using this OID, see [WWAN Driver Initialization Procedure](https://msdn.microsoft.com/library/windows/hardware/ff557186).

Miniport drivers can access device memory when processing query operations, but should not access the provider network or the Subscriber Identity Module (SIM card).

Many "world-wide" MB devices today support multiple frequency bands because the frequency bands for 2.5G/3G vary from country to country. The list of all the radio frequencies specified in the 3GPP standards (for GSM-based networks) and 3GPP2 standards (for CDMA-based networks) is shown in the following tables. Both standards adopt a similar band classification scheme.

**3GPP (GSM-based) Frequency Band Classes**

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th>3GPP band</th>
<th>Designated spectrum</th>
<th>Industry name</th>
<th>Uplink (MS to BTS)</th>
<th>Downlink (BTS to MS)</th>
<th>Regions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Band I</p></td>
<td><p>UMTS2100</p></td>
<td><p>IMT</p></td>
<td><p>1920-1980</p></td>
<td><p>2110-2170</p></td>
<td><p>Europe, Korea, Japan, China</p></td>
</tr>
<tr class="even">
<td><p>Band II</p></td>
<td><p>UMTS1900</p></td>
<td><p>PCS1900</p></td>
<td><p>1850-1910</p></td>
<td><p>1930-1990</p></td>
<td><p>North America, LATAM</p></td>
</tr>
<tr class="odd">
<td><p>Band III</p></td>
<td><p>UMTS1800</p></td>
<td><p>DCS1800</p></td>
<td><p>1710-1785</p></td>
<td><p>1805-1880</p></td>
<td><p>Europe, China</p></td>
</tr>
<tr class="even">
<td><p>Band IV</p></td>
<td><p>AWS</p></td>
<td><p>AWS, 1.7/2.1</p></td>
<td><p>1710-1755</p></td>
<td><p>2110-2155</p></td>
<td><p>North America, LATAM</p></td>
</tr>
<tr class="odd">
<td><p>Band V</p></td>
<td><p>UMTS850</p></td>
<td><p>GSM850</p></td>
<td><p>824-849</p></td>
<td><p>869-894</p></td>
<td><p>North America, LATAM</p></td>
</tr>
<tr class="even">
<td><p>Band VI</p></td>
<td><p>UMTS800</p></td>
<td><p>UMTS800</p></td>
<td><p>830-840</p></td>
<td><p>875-885</p></td>
<td><p>Japan</p></td>
</tr>
<tr class="odd">
<td><p>Band VII</p></td>
<td><p>UMTS2600</p></td>
<td><p>UMTS2600</p></td>
<td><p>2500-2570</p></td>
<td><p>2620-2690</p></td>
<td><p>Europe</p></td>
</tr>
<tr class="even">
<td><p>Band VIII</p></td>
<td><p>UMTS900</p></td>
<td><p>EGSM900</p></td>
<td><p>880-915</p></td>
<td><p>925-960</p></td>
<td><p>Europe, China</p></td>
</tr>
<tr class="odd">
<td><p>Band IX</p></td>
<td><p>UMTS1700</p></td>
<td><p>UMTS1700</p></td>
<td><p>1750-1785</p></td>
<td><p>1845-1880</p></td>
<td><p>Japan</p></td>
</tr>
<tr class="even">
<td><p>Band X</p></td>
<td></td>
<td></td>
<td><p>1710-1770</p></td>
<td><p>2110-2170</p></td>
<td></td>
</tr>
</tbody>
</table>

 

**3GPP2 (CDMA-based) Frequency Band Classes**

3GPP band
Industry name
Uplink (MS to BTS)
Downlink (BTS to MS)
Band 0

800MHz Cellular

824.025-844.995

869.025-889.995

Band I

1900MHz Band

1850-1910

1930-1990

Band II

TACS Band

872.025-914.9875

917.0125-959.9875

Band III

JTACS Band

887.0125-924.9875

832.0125-869.9875

Band IV

Korean PCS Band

1750 - 1780

1840 - 1870

Band V

450 MHz Band

410 - 483.475

420 - 493.475

Band VI

2 GHz Band

1920 - 1979.950

2110 - 2169.950

Band VII

700 MHz Band

776 - 794

746 - 764

Band VIII

1800 MHz Band

1710 - 1784.950

1805 - 1879.95

Band IX

900 MHz Band

880 - 914.950

925 - 959.950

Band X

Secondary 800 MHz Band

806 - 900.975

851 - 939.975

Band XI

400 MHz European PAMR Band

410 - 483.475

420 - 493.475

Band XII

800 MHz PAMR Band

870.125 - 875.9875

915.0125 - 920.9875

Band XIII

2.5GHz IMT2000 Extension Band

2500 - 2570

2620 - 2690

Band XIV

US PCS 1.9GHz Band

1850 - 1915

1930 - 1995

Band XV

AWS Band

1710 - 1755

2110 - 2155

Band XVI

US 2.5GHz Band

2502 - 2568

2624 - 2690

Band XVII

US 2.5 GHz Forward Link Only Band

2624-2690

 

The unit for radio frequency bands in both tables is megahertz (MHz).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567907)

[WWAN Driver Initialization Procedure](https://msdn.microsoft.com/library/windows/hardware/ff557186)

 

 




