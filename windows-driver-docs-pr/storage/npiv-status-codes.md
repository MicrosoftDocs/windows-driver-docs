---
title: NPIV Status Codes (Windows Drivers)
description: Learn more about NPIV Status Codes.
keywords:
- NPIV_AUTHENTICATION_FAILED
- NPIV_HASH_FUNCTION_NOT_USABLE
- NPIV_AUTHENTICATION_TRANSACTION_ALREADY_STARTED
- NPIV_AUTHENTICATION_MECHANISM_NOT_USABLE
- NPIV_LINK_DOWN
- NPIV_UNKNOWN_ERROR
- NPIV_OUT_OF_RESOURCES
- NPIV_WWPN_IN_USE
- NPIV_NOT_SUPPORTED_FABRIC
- NPIV_UNSUPPORTED_PROTOCOL_VERSION
- NPIV_SUCCESS
- NPIV_NOT_SUPPORTED_HOST
- NPIV_MAX_VPORT_COUNT
- NPIV_WWPN_NOT_FOUND
- NPIV_WWPN_INVALID_FORMAT
ms.date: 10/14/2022
---

# NPIV Status Codes

The NPIV WMI methods return the result of a port operation in their *Status* out parameter. The status values and descriptions are the following.

<table>
<thead>
<tr class="header">
<th>Return code/value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="NPIV_SUCCESS"></span><span id="npiv_success"></span>
<strong>NPIV_SUCCESS</strong>
0x0</td>
<td><p>The NPIV virtual port operation completed successfully.</p></td>
</tr>
<tr class="even">
<td><span id="NPIV_UNKNOWN_ERROR"></span><span id="npiv_unknown_error"></span>
<strong>NPIV_UNKNOWN_ERROR</strong>
0x1</td>
<td><p>The NPIV virtual port operation failed with an unknown error.</p></td>
</tr>
<tr class="odd">
<td><span id="NPIV_NOT_SUPPORTED_HOST"></span><span id="npiv_not_supported_host"></span>
<strong>NPIV_NOT_SUPPORTED_HOST</strong>
0x2</td>
<td><p>The NPIV virtual port operation is not supported by the host</p></td>
</tr>
<tr class="even">
<td><span id="NPIV_NOT_SUPPORTED_FABRIC"></span><span id="npiv_not_supported_fabric"></span>
<strong>NPIV_NOT_SUPPORTED_FABRIC</strong>
0x3</td>
<td><p>The NPIV virtual port operation is not supported by the fabric.</p></td>
</tr>
<tr class="odd">
<td><span id="NPIV_OUT_OF_RESOURCES"></span><span id="npiv_out_of_resources"></span>
<strong>NPIV_OUT_OF_RESOURCES</strong>
0x4</td>
<td><p>There are not enough of resources to perform the NPIV virtual port operation.</p></td>
</tr>
<tr class="even">
<td><span id="NPIV_MAX_VPORT_COUNT"></span><span id="npiv_max_vport_count"></span>
<strong>NPIV_MAX_VPORT_COUNT</strong>
0x5</td>
<td><p>The maximum number of virtual ports on the physical HBA is exceeded.</p></td>
</tr>
<tr class="odd">
<td><span id="NPIV_WWPN_IN_USE"></span><span id="npiv_wwpn_in_use"></span>
<strong>NPIV_WWPN_IN_USE</strong>
0x6</td>
<td><p>The world wide port name already exists on the fabric.</p></td>
</tr>
<tr class="even">
<td><span id="NPIV_WWPN_INVALID_FORMAT"></span><span id="npiv_wwpn_invalid_format"></span>
<strong>NPIV_WWPN_INVALID_FORMAT</strong>
0x7</td>
<td><p>An invalid parameter was given.</p></td>
</tr>
<tr class="odd">
<td><span id="NPIV_LINK_DOWN"></span><span id="npiv_link_down"></span>
<strong>NPIV_LINK_DOWN</strong>
0x8</td>
<td><p>The fibre channel link is down.</p></td>
</tr>
<tr class="even">
<td><span id="NPIV_WWPN_NOT_FOUND"></span><span id="npiv_wwpn_not_found"></span>
<strong>NPIV_WWPN_NOT_FOUND</strong>
0x9</td>
<td><p>The fibre channel miniport driver does not support NPIV or the NPIV WMI classes are not installed correctly.</p></td>
</tr>
<tr class="odd">
<td><span id="NPIV_AUTHENTICATION_MECHANISM_NOT_USABLE"></span><span id="npiv_authentication_mechanism_not_usable"></span>
<strong>NPIV_AUTHENTICATION_MECHANISM_NOT_USABLE</strong>
0xA</td>
<td><p>The DH-CHAP authentication mechanism is not usable.</p></td>
</tr>
<tr class="even">
<td><span id="NPIV_HASH_FUNCTION_NOT_USABLE"></span><span id="npiv_hash_function_not_usable"></span>
<strong>NPIV_HASH_FUNCTION_NOT_USABLE</strong>
0xB</td>
<td><p>The DH-CHAP hash function is not usable.</p></td>
</tr>
<tr class="odd">
<td><span id="NPIV_AUTHENTICATION_TRANSACTION_ALREADY_STARTED"></span><span id="npiv_authentication_transaction_already_started"></span>
<strong>NPIV_AUTHENTICATION_TRANSACTION_ALREADY_STARTED</strong>
0xC</td>
<td><p>The DH-CHAP authentication transaction has already started</p></td>
</tr>
<tr class="even">
<td><span id="NPIV_AUTHENTICATION_FAILED"></span><span id="npiv_authentication_failed"></span>
<strong>NPIV_AUTHENTICATION_FAILED</strong>
0xD</td>
<td><p>The DH-CHAP authentication for the virtual port failed.</p></td>
</tr>
<tr class="odd">
<td><span id="NPIV_UNSUPPORTED_PROTOCOL_VERSION"></span><span id="npiv_unsupported_protocol_version"></span>
<strong>NPIV_UNSUPPORTED_PROTOCOL_VERSION</strong>
0xE</td>
<td><p>The specified NPIV protocol version is not supported.</p></td>
</tr>
</tbody>
</table>
