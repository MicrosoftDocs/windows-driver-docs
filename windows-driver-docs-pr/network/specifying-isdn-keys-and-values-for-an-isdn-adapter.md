---
title: Specifying ISDN Keys and Values for an ISDN Adapter
description: Specifying ISDN Keys and Values for an ISDN Adapter
ms.assetid: ba2156c1-fb54-4e1e-b0ec-72aa2d950505
keywords:
- add-registry-sections WDK networking , ISDN adapters
- ISDN adapters WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying ISDN Keys and Values for an ISDN Adapter





In addition to a **WanEndpoints** value, an INF file for an ISDN adapter must add (through an *add-registry-section*) the following keys and values to the instance key for the adapter. For more information, see [Specifying WAN Endpoints for a WAN Adapter](specifying-wan-endpoints-for-a-wan-adapter.md).

**Note**   ISDN drivers are deprecated in Windows 8.1, Windows Server 2012 R2, and later.



-   **IsdnNumDChannels**

    Specifies the number of D-channels that are supported by the ISDN adapter.

-   **IsdnAutoSwitchDetect** (Optional)

    Specifies whether the ISDN adapter supports automatic switch detection. A value of 1 indicates that the adapter supports automatic switch detection. A value of zero indicates that the adapter does not support automatic switch detection.

-   **IsdnSwitchTypes**

    Specifies the switch types that are supported by the ISDN adapter.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Switch</th>
    <th align="left">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_AUTO</p></td>
    <td align="left"><p>Auto Detect (North America only)</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_ATT</p></td>
    <td align="left"><p>ESS5 (AT&T, North America)</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_NI1</p></td>
    <td align="left"><p>National ISDN 1 (NI-1)</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_NI2</p></td>
    <td align="left"><p>National ISDN 2 (NI-2)</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_NT1</p></td>
    <td align="left"><p>Northern Telecom DMS 100 (NT-1)</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_INS64</p></td>
    <td align="left"><p>NTT INS64 (Japan)</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_1TR6</p></td>
    <td align="left"><p>German National (1TR6). This switch type is rarely used.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_VN3</p></td>
    <td align="left"><p>French National (VN3). This switch type is rarely used.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_NET3</p></td>
    <td align="left"><p>European ISDN (DSS1)</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_DSS1</p></td>
    <td align="left"><p>European ISDN (DSS1)</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_AUS</p></td>
    <td align="left"><p>Australian National. This switch type is rarely used.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_BEL</p></td>
    <td align="left"><p>Belgium National. This switch type is rarely used.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_VN4</p></td>
    <td align="left"><p>French National (VN4)</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_SWE</p></td>
    <td align="left"><p>Swedish National</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>ISDN_SWITCH_ITA</p></td>
    <td align="left"><p>Italian National</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>ISDN_SWITCH_TWN</p></td>
    <td align="left"><p>Taiwanese</p></td>
    </tr>
    </tbody>
    </table>




To specify multiple switch types, simply add the individual switch type values together.

The ISDN Wizard, which runs automatically during the installation of an ISDN component, allows the user to select one of the switch types specified by **IsdnSwitchTypes**. The selected switch type determines which other ISDN parameters the ISDN Wizard subsequently displays for configuration. These ISDN parameters include the phone number, the SPID (service profile identifier), the subaddress, and the multisubscriber number.


-   An **IsdnNumBChannels** value and a *D-channel* key for each D-channel

    The *D-channel* key is an zero-based index from 0 through 9 that identifies the D-channel. **IsdnNumBChannels** is a REG\_DWORD value added to the *D-channel* key. **IsdnNumBChannels** specifies the number of B-channels supported by the D-channel.

The following is an example of an *add-registry-section* that adds ISDN keys and values to the instance key of an ISDN adapter. Two D-channels are specified for the adapter, and two B-channels are specified for each D-channel.

```INF
[ISDNadapter.reg]
HKR,,  WanEndPoints,         0x00010001, 4
HKR,,  IsdnNumDChannels,     0x00010001, 2
HKR,,  IsdnAutoSwitchDetect, 0x00010001, 1
HKR,,  IsdnSwitchTypes,      0x00010001, 0x00000004  ;NI1

HKR, 0, IsdnNumBChannels,    0x00010001, 2

HKR, 1, IsdnNumBChannels,    0x00010001, 2
```

The ISDN Wizard itself also adds ISDN keys and values to the instance key for an ISDN adapter, based on the parameter values specified by the user. The ISDN Wizard adds the following keys and values:

-   **IsdnSwitchType**

    A REG\_DWORD that indicates the switch type that was selected by the user for the ISDN adapter.

-   **IsdnMultiSubscriberNumbers** value for each D-channel

    A REG\_MULTI\_SZ value that indicates the multisubscriber numbers that were specified by the user for the D-channel.

-   A *B-channel* key and an **IsdnSpid**, **IsdnPhoneNumber**, and/or an **IsdnSubaddress** value for each B-channel:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Key or Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>B-channel</em> key</p></td>
<td align="left"><p>A zero-based index that identifies the B-channel. The maximum value for a <em>B-channel</em> key is one less than the <strong>IsdnNumBchannels</strong> value assigned to the D-channel to which the B-channel belongs.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IsdnSpid</strong></p></td>
<td align="left"><p>A REG_SZ value that indicates the SPID, if any, specified by the user for the B-channel.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IsdnPhoneNumber</strong></p></td>
<td align="left"><p>The phone number, if any, specified by the user for the B-channel.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IsdnSubaddress</strong></p></td>
<td align="left"><p>The subaddress, if any, specified by the user for the B-channel.</p></td>
</tr>
</tbody>
</table>



The following example is an ISDN adapter's registry section layout . Each registry key is enclosed in square brackets, for example: \[ *KeyName* \]. The ISDN keys and values that were added by the INF file for the ISDN adapter are highlighted in boldface text; the ISDN keys and values that were added by the ISDN Wizard appear in normal (nonboldface) text.

```INF
[...Enum\emumeratorID\device-instance-id]  ;ISDN adapter instance key
WanEndpoints=4
IsdnNumDChannels=2
IsdnAutoSwitchDetect=1
IsdnSwitchType=0x4  ;National ISDN 1

[...Enum\emumeratorID\device-instance-id\0]  ;D-channel 0
IsdnNumBChannels=2
IsdnMultiSubscriberNumbers=1234567 2345678 3456789

[...Enum\emumeratorID\device-instance-id\0\0]  ;B-channel 0 for D-channel 0
IsdnSpid=00555121200
IsdnPhoneNumber=5551212
IsdnSubaddress=

[...Enum\emumeratorID\device-instance-id\0\1]  ;B-channel 1 key for D-channel 0
IsdnSpid=00555121300
IsdnPhoneNumber=5551213
IsdnSubaddress=

[...Enum\emumeratorID\device-instance-id\1]  ;D-channel 1 key
IsdnNumBChannels=2
IsdnMultiSubscriberNumbers=8675309 2390125 7658156

[...Enum\emumeratorID\device-instance-id\1\0]  ;B-channel 0 for D-channel 1
IsdnSpid=00555987600
IsdnPhoneNumber=5559876
IsdnSubaddress=

[...Enum\emumeratorID\device-instance-id\1\0]  ;B-channel 1 for D-channel 1
IsdnSpid=00555876500
IsdnPhoneNumber=5558765
IsdnSubaddress=
```









