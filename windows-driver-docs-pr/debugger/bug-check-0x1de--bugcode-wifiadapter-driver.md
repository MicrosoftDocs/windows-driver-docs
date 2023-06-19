---
title: Bug Check 0x1DE BUGCODE_WIFIADAPTER_DRIVER
description: The BUGCODE_WIFIADAPTER_DRIVER bug check has a value of 0x000001DE. This indicates that the operating system encountered an error caused by a networking driver managed by WiFiAdapterCx.
keywords: ["Bug Check 0x1DE BUGCODE_WIFIADAPTER_DRIVER", "BUGCODE_WIFIADAPTER_DRIVER"]
ms.date: 03/15/2023
topic_type:
- apiref
api_name:
- BUGCODE_WIFIADAPTER_DRIVER
api_type:
- NA
---

# Bug Check 0x1DE: BUGCODE\_WIFIADAPTER\_DRIVER

The BUGCODE\_WIFIADAPTER\_DRIVER bug check has a value of 0x000001DE. This indicates that the operating system encountered an error caused by a networking driver managed by WiFiCx. The Wi-Fi WDF class extensions (WiFiCx) supports KMDF-based Wi-Fi client driver for Wi-Fi devices.  For more information, see [Introduction to the Wi-Fi WDF class extension (WiFiCx)](../netcx/wifi-wdf-class-extension-wificx.md).

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## BUGCODE\_WIFIADAPTER\_DRIVER Parameters

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>WiFiCx BugCheck subcode values listed here.</p>
<p>0x0 - The WiFiCx private globals have been corrupted. </p>
<p></p>
<p>0x1 : A driver called a WiFiCx API requiring passive IRQL at illegal IRQL. <BR>
    2 - The current IRQL. </p>
<p></p>
<p>0x2 : A driver called a WiFiCx API requiring IRQL less than or equal to dispatch at illegal IRQL. <BR>
2 - The current IRQL. </p>
<p></p>
0x3 : A struct with invalid size was passed to WiFiCx API. <BR>
  2 - Size of struct passed by the driver.<BR>
 3 - Size of struct used by OS's WiFiCx version. Note that it is not required that this matches exactly,
            with the passed struct, but the size of structs from older WiFiCx versions should be <=
            than those from newer versions.</p>
<p></p>
<p>0x4 : The driver reported and invalid wake reason. <BR>
        2 - The reported wake reason.</p>
<p></p>
<p>0x5 : The driver passed an invalid or corrupted WIFI_POWER_OFFLOAD_LIST to a WiFiCx API. <BR>
        2 - Pointer to WIFI_POWER_OFFLOAD_LIST.
 </p>
<p> </p>
<p>0x6 : The driver passed an invalid or corrupted WIFI_WAKE_SOURCE_LIST to a WiFiCx API. <BR>
        2 - Pointer to WIFI_WAKE_SOURCE_LIST.
</p>
<p></p>
<p>0x7 : The driver passed an invalid or uninitialized WIFI_INTERFACE_CONTEXT to a WiFiCx API. <BR>
        2 - Pointer to the passed WIFI_INTERFACE_CONTEXT.
</p>
<p></p>
<p>0x8 : The driver passed a WIFI_ADAPTER_TX_DEMUX with an invalid WIFI_ADAPTER_TX_DEMUX_TYPE to a WiFiCx API.<BR>
2 - Pointer to the passed WIFI_ADAPTER_TX_DEMUX.<BR>
3 - The passed WIFI_ADAPTER_TX_DEMUX's WIFI_ADAPTER_TX_DEMUX_TYPE.
</p>
<p></p>
<p>0x9 : The driver passed a WIFI_ADAPTER_TX_DEMUX with an invalid Range to a WiFiCx API.<BR>
        2 - Pointer to the passed WIFI_ADAPTER_TX_DEMUX.<BR>
        3 - The passed WIFI_ADAPTER_TX_DEMUX's Range.
</p>
<p></p>
<p>0xA : The driver reported a wake reason at an invalid time. Wake reasons should be reported from within the disarm wake callback.
</p>
<p>0xB : The driver is using a deprecated field within a WiFiCx struct.<BR>
        2 - Pointer to string representing deprecated field in use.   </p>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Dependent on Param 1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Dependent on Param 1</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bugcheck and can be helpful in determining the root cause.

Parameter 1 describes the type of violation. Look at the call stack to determine the misbehaving driver.

## See also

[Introduction to the Wi-Fi WDF class extension (WiFiCx)](../netcx/wifi-wdf-class-extension-wificx.md)

[Bug Check Code Reference](bug-check-code-reference2.md)