---
title: Extended Capabilities from a WDM Audio Driver
description: Extended Capabilities from a WDM Audio Driver
ms.assetid: 8ee081ee-623d-4eaf-953f-20ccfbbe9800
keywords:
- WDM audio extensions WDK , about legacy support extensions
- WDM audio extensions WDK , device IDs
- device IDs WDK audio
- unique device IDs WDK audio
- identifying audio devices
- hardware-specific information WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Capabilities from a WDM Audio Driver


## <span id="extended_capabilities_from_a_wdm_audio_driver"></span><span id="EXTENDED_CAPABILITIES_FROM_A_WDM_AUDIO_DRIVER"></span>


By handling the [**KSPROPERTY\_GENERAL\_COMPONENTID**](https://msdn.microsoft.com/library/windows/hardware/ff565171) property, an audio filter can provide hardware-specific information that applications can use to uniquely identify the underlying device. Microsoft Windows XP is the first version of Windows to support this feature; this feature is not available in earlier versions.

The filter provides the hardware-specific information in the form of a [**KSCOMPONENTID**](https://msdn.microsoft.com/library/windows/hardware/ff561027) structure that contains the following:

-   Manufacturer GUID

-   Product GUID

-   Component GUID

-   Name GUID

-   Hardware version number

-   Hardware revision number

To provide access to this information, a WDM audio driver specifies a property handler for KSPROPERTY\_GENERAL\_COMPONENTID in the filter automation table.

An application can access the data from the driver's KSCOMPONENTID structure through the following legacy Windows multimedia APIs: **aux**, **midiIn**, **midiOut**, **mixer**, **waveIn**, and **waveOut**. A client queries the driver for this information by calling one of the multimedia functions in the following table and passing in an extended-capabilities structure as the second argument.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Multimedia Function</th>
<th align="left">Extended-Capabilities Structure</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>auxGetDevCaps</strong></p></td>
<td align="left"><p>AUXCAPS2</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>midiInGetDevCaps</strong></p></td>
<td align="left"><p>MIDIINCAPS2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>midiOutGetDevCaps</strong></p></td>
<td align="left"><p>MINIOUTCAPS2</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>mixerGetDevCaps</strong></p></td>
<td align="left"><p>MIXERCAPS2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>waveInGetDevCaps</strong></p></td>
<td align="left"><p>WAVEINCAPS2</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>waveOutGetDevCaps</strong></p></td>
<td align="left"><p>WAVEOUTCAPS2</p></td>
</tr>
</tbody>
</table>

 

After receiving the KSCOMPONENTID structure from the filter's property handler, the WDMAud system driver (Wdmaud.sys) converts the data from this structure to the *XXX*CAPS2 format that the *xxx*GetDevCaps functions use.

After verifying that the capabilities structure passed to the function is large enough to contain the manufacturer, product, and name GUIDs, the *xxx*GetDevCaps function copies this information into the extended structure before returning. (The component GUID from KSCOMPONENTID currently is not used.)

WDMAud concatenates the **Version** and **Revision** members from KSCOMPONENTID to form the 16-bit revision number that the *xxx*GetDevCaps function copies into the **vDriverVersion** member of the capabilities structure:

**vDriverVersion** = (**Version** &lt;&lt; 8) | (**Revision** & 0xFF)

Microsoft previously required vendors to register manufacturer IDs and product IDs for their audio devices. These IDs were then released in the header file Mmreg.h.

In Windows XP and later, registered IDs are no longer necessary; they are replaced by the manufacturer and product GUIDs that are provided through the KSPROPERTY\_GENERAL\_COMPONENTID property. The GUIDs are more convenient for vendors to use than registered IDs because GUIDs are inherently unique, are easily generated, and require no registration.

However, if you have already registered product and manufacturer IDs with Microsoft (and they are in Mmreg.h), you can use the macros INIT\_MMREG\_PID and INIT\_MMREG\_MID in Ksmedia.h to convert your product and manufacturer IDs into GUIDs. If you use these macros to generate the GUIDs, WDMAud is able to recover the original product and manufacturer IDs from the GUIDs and copy these IDs into the **wPid** and **wMid** members of the capabilities structure that is filled in by the *xxx*GetDevCaps call.

Otherwise, if you do not have registered manufacturer and product IDs, simply use the GuidGen utility to generate the manufacturer and product GUIDs. (GuidGen is included in the Microsoft Windows SDK.) When a driver's GUIDs are of this type, WDMAud loads default constants MM\_UNMAPPED and MM\_PID\_UNMAPPED into the **wMid** and **wPid** members, respectively, of the capabilities structure that is filled in by the *xxx*GetDevCaps call.

WDMAud uses the **Name** GUID in the KSCOMPONENTID structure to look up a "Name" key in the registry. This key is located under the registry path name HKLM\\System\\CurrentControlSet\\Control\\MediaCategories. The "Name" key for a device has an associated string value that contains the device name. The *xxx*GetDevCaps function copies the first 31 characters of this name string into the **szPname** member of the capabilities structure. For device names longer than 31 characters, a client application can open the registry key and directly read the entire string. A driver can populate this registry entry in one of two ways:

-   The driver can specify the entry in the device's INF file at install time.

-   The driver can load the entry during execution of its filter-initialization routine.

The name GUID is optional. If the driver sets the **Name** member in the KSCOMPONENTID to the GUID\_NULL value, WDMAud provides the device's friendly name to the *xxx*GetDevCaps function, which copies this name into the **szPname** member of the capabilities structure.

If the filter exposes no handler for the KSPROPERTY\_GENERAL\_COMPONENTID property, WDMAud uses default values in place of the data from the KSCOMPONENTID structure. The default values for the legacy portion of the capabilities structure are as follows:

-   **wMid** = MM\_MICROSOFT

-   **wPid** = a device class from the following list:
    MM\_MSFT\_WDMAUDIO\_WAVEOUT
    MM\_MSFT\_WDMAUDIO\_WAVEIN
    MM\_MSFT\_WDMAUDIO\_MIDIOUT
    MM\_MSFT\_WDMAUDIO\_MIDIIN
    MM\_MSFT\_WDMAUDIO\_MIXER
    MM\_MSFT\_WDMAUDIO\_AUX
-   **vDriverVersion** = 0x050a (for Windows XP) or 0x0500 (pre-Windows XP)

On Windows releases earlier than Windows XP, the legacy members of the capabilities structure are always set to the defaults above. On Windows XP and later, the default values for the extended capabilities are as follows:

-   **NameGuid** = GUID\_NULL

-   INIT\_MMREG\_MID(&**ManufacturerGuid**, **wMid**)

-   INIT\_MMREG\_PID(&**ProductGuid**, **wPid**)

The INIT\_MMREG\_MID and INIT\_MMREG\_PID macros above are defined in Ksmedia.h. These macros are used to convert the manufacturer and product IDs in the **wMid** and **wPid** members to GUIDs that are loaded into the **ManufacturerGuid** and **ProductGuid** members.

 

 




