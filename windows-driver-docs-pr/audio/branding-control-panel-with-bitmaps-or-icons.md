---
title: Branding Control Panel with Bitmaps or Icons
description: Branding Control Panel with Bitmaps or Icons
ms.assetid: 1520cf9e-6813-41aa-aa88-39a1a6c27f74
keywords:
- audio adapters WDK , control-panel branding
- adapter drivers WDK audio , control-panel branding
- Port Class audio adapters WDK , control-panel branding
- control-panel branding WDK audio
- branding device controls WDK audio
- thrid-party branding WDK audio
- vendor branding WDK audio
- logo branding WDK audio
- icons WDK audio
- bitmap branding WDK audio
- image branding WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Branding Control Panel with Bitmaps or Icons


## <span id="control_panel_branding_by_vendors"></span><span id="CONTROL_PANEL_BRANDING_BY_VENDORS"></span>


In Windows XP and later versions of Windows, the sound application in Control Panel supports third-party branding of audio-device controls. Independent hardware vendors (IHVs) can display the following items next to the controls for their audio devices:

-   Company logo

-   Proprietary device name

The INF file that installs the device driver also loads the Control Panel customization data into the registry. Bitmapped images of company logos are contained in the installed driver files themselves.

In Windows XP, branding information is visible to users in the following program locations:

-   The **Volume** page of the **Sounds and Audio Devices** application in Control Panel (Mmsys.cpl)

-   The SndVol32 program (Sndvol32.exe)

In Windows Vista, branding information is visible to users in the **Playback** and **Recording** pages of the *Sound* application in Control Panel (Mmsys.cpl).

The branding information is stored in the registry in a **Branding** subkey under the audio device's root key, which is located under the media-class key. The **Branding** subkey can contain one or more of the REG\_SZ values that are shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value name</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>icon</p></td>
<td align="left"><p>Name of the file that contains the icon that is used by the SndVol32 control menu.</p></td>
</tr>
<tr class="even">
<td align="left"><p>bitmap</p></td>
<td align="left"><p>Name of the file that contains the 32-by-32 bitmap that is displayed in the <strong>Volume</strong> page of the <strong>Sound and Audio Devices</strong> application in Control Panel.</p></td>
</tr>
</tbody>
</table>

 

These values are added to the registry by directives within the add-registry-section (see [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)) of the INF file that installs the device driver. Control Panel uses defaults for any values that are missing from the **Branding** subkey.

The "bitmap" logo appears to the left of the proprietary device name at the top of the **Volume** page. The "icon" logo appears in the top-left corner of the SndVol32 control menu.

The proprietary device name that appears in the previously mentioned pages is the friendly name of the device. This friendly name is specified by a directive in the add-registry-section of the INF file that installs the device. This directive contains the keyword "FriendlyName", as shown in the example in [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320). In Windows XP, the **Volume** page and SndVol32 display only the first 31 characters of the name string. Longer strings are truncated. In Windows Vista and later versions of Windows, this 31-character restriction is removed when the device name is displayed in Control Panel. When you use APIs that were supported in versions of Windows earlier than Windows Vista, for example [MCI\_GetDevCaps](https://go.microsoft.com/fwlink/p/?linkid=149692), the 31-character limit still applies to the device name that you provide to the API.

**Important**   In Windows Vista and later versions of Windows, the use of bitmap images for third-party branding is no longer supported. Third-party audio driver developers who want to brand their audio device controls must use icons. The supported pixel dimensions for these icons are 32x32 or 48x48.

 

### <span id="Example_1"></span><span id="example_1"></span><span id="EXAMPLE_1"></span>Example 1

The following example shows a couple of directives from the add-registry-section of a vendor's INF file:

```inf
  [XYZ-Audio-Device.AddReg]
  HKR,Branding,icon,,"foo.sys,102"
  HKR,Branding,bitmap,,"c:\mydir\myimage.bmp"
```

These directives add control-panel branding information to the registry. HKR represents the audio device's root key in the registry; the **Branding** subkey is specified relative to the path name for the root key. The string value for the **icon** or **bitmap** key can be specified in one of two formats: "file,resourceid" or "imagefile". The first directive in the preceding example uses the "file,resourceid" format. The directive assigns to the **icon** key a string value that contains a file name, foo.sys, and a resource ID of 102. The file name and resource ID are separated by a comma (with no spaces). The file foo.sys contains the icon resource. The second directive in the preceding example assigns an "imagefile" formatted string to the **bitmap** key; the string contains the full path name of a .bmp file that contains the bitmap.

The example directive for the **icon** value can be changed to use the "imagefile" format, but in this case the string value should contain the path name of a file with an .ico file name extension.

In the case of the "file,resourceid" format, the control-panel software searches the same list of the search paths as the **LoadLibrary** function (described in the Microsoft Windows SDK documentation). If this path list does not contain the file, the software also searches the drivers directory (see [**INF DestinationDirs Section**](https://msdn.microsoft.com/library/windows/hardware/ff547383)). This format allows the images to be easily stored in the driver file itself without requiring that absolute path names be specified in the INF file.

### <span id="example_2"></span><span id="EXAMPLE_2"></span> Example 2

The following example applies to Windows Vista and later versions of Windows. This example shows a directive from the add-registry-section of a vendor's INF file. This example uses the "imagefile" format:

```inf
[ABC-Audio-Device.AddReg]
  HKR,Branding,icon,,"c:\mydir\myicon.ico"
```

 

 




