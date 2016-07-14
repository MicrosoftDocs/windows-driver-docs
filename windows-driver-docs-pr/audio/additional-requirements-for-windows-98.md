---
Description: Additional Requirements for Windows 98
MS-HAID: 'audio.additional\_requirements\_for\_windows\_98'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Additional Requirements for Windows 98
---

# Additional Requirements for Windows 98


## <span id="additional_requirements_for_windows_98"></span><span id="ADDITIONAL_REQUIREMENTS_FOR_WINDOWS_98"></span>


In Microsoft Windows 98, a bug in the system graph builder prevents a KSCATEGORY\_AUDIO\_DEVICE wave-data path from operating correctly unless it contains at least one node. Because PCM pins are either hardware mixing pins (with SUM, volume, and SRC nodes, for example; see [**KSNODETYPE\_SUM**](audio.ksnodetype_sum), [**KSNODETYPE\_VOLUME**](audio.ksnodetype_volume), and [**KSNODETYPE\_SRC**](audio.ksnodetype_src)) or have KMixer (and its nodes) inserted above them, this problem affects non-PCM pins only. In order for your driver to work on Windows 98 SE + hotfix, make sure that the data path through a non-PCM pin always has at least one node. When passing AC-3 over S/PDIF, for example, you can add a KSNODETYPE\_SPDIF\_INTERFACE node that implements a property to manipulate the serial copy management system (SCMS) bits in the S/PDIF digital output stream.

The earliest hot-fix package for Windows 98 SE that contains the fix to enable AC-3 playback over S/PDIF is the following:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Hot-Fix Number</th>
<th align="left">Executable File</th>
<th align="left">Release Date</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WinSE 9724</p></td>
<td align="left"><p>269601USA8.EXE</p></td>
<td align="left"><p>8/9/2000</p></td>
</tr>
</tbody>
</table>

 

All later hot-fix packages for Windows 98 SE also contain this fix.

This hot-fix package installs updated versions of the following audio system files:

-   Kmixer.sys

-   Portcls.sys

-   Sbemul.sys

-   Sysaudio.sys

-   Usbaudio.sys

-   Wdmaud.sys

-   Wdmaud.drv

The [IPortClsVersion](audio.iportclsversion) interface is not available in this hotfix, which means that this interface cannot be used to detect the presence of the hotfix.

The best way to determine whether a hotfix that contains the WavePci fixes is present is as follows:

-   Verify that the operating system is Windows 98 Second Edition.

-   Check the file version and/or date of Portcls.sys.

The WavePci fixes are present in the following the file version and date of Portcls.sys (or in any more recent version):

-   File Version: 4.10.2223

-   Date Created: 3/21/2000 8:34:03 PM

Another technique is to look in the registry to determine whether a particular hotfix has been installed. For example, you can try to access the following registry key to see whether the first hot-fix package for Windows 98 SE is installed:

```
    HKLM\Software\Microsoft\Windows\CurrentVersion\Setup\Updates\W98.SE\UPD\269601
```

The key exists only if the first hot-fix package is installed. The drawback to this approach is that it does not tell you whether a later hot-fix package, which also includes the WavePci fixes, is installed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Additional%20Requirements%20for%20Windows%2098%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



