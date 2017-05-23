---
title: gdikdx.verifier
description: The gdikdx.verifier extension displays the status of Driver Verifier during the verification of a graphics driver.
ms.assetid: a7e189bb-ed63-4da3-ab7a-bf502ec131ed
keywords: ["gdikdx.verifier Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- gdikdx.verifier
api_type:
- NA
---

# !gdikdx.verifier


The **!gdikdx.verifier** extension displays the status of Driver Verifier during the verification of a graphics driver.

``` syntax
    !gdikdx.verifier [-Flags] 
```

## <span id="ddk__gdikdx_verifier_dbg"></span><span id="DDK__GDIKDX_VERIFIER_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what information will be displayed in the output from this command. Any combination of the following (preceded by a hyphen) is allowed:

<span id="d"></span><span id="D"></span>**d**  
Causes the display to include statistics on **Memory Pool Tracking**. This includes the address, size, and tag of each pool.

<span id="h__or___"></span><span id="H__OR___"></span>**h** (or **?**)  
Displays some brief Help text for this command in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Gdikdx.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about Driver Verifier, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

When verifying drivers that are not graphics drivers, the standard kernel-mode extension [**!verifier**](-verifier.md) should be used instead of **!gdikdx.verifier**.

Regardless of which flags are selected, this extension will display the Driver Verifier options that are active. It will also display statistics on the frequency of random failure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!gdikdx.verifier%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




