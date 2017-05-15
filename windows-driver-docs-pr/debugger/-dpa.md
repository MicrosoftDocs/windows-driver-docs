---
title: dpa
description: The dpa extension displays pool allocation information.
ms.assetid: 1eb31741-bc50-4188-823d-b6324d2dfdf1
keywords: ["pool allocation", "dpa Windows Debugging"]
topic_type:
- apiref
api_name:
- dpa
api_type:
- NA
---

# !dpa


The **!dpa** extension displays pool allocation information.

``` syntax
!dpa Options 
!dpa -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Must be exactly one of the following options:

<span id="-c"></span><span id="-C"></span>**-c**  
Displays current pool allocation statistics.

<span id="-v"></span><span id="-V"></span>**-v**  
Displays all current pool allocations.

<span id="-vs"></span><span id="-VS"></span>**-vs**  
Causes the display to include stack traces.

<span id="-f"></span><span id="-F"></span>**-f**  
Displays failed pool allocations.

<span id="-r"></span><span id="-R"></span>**-r**  
Displays free pool allocations.

<span id="-p_Ptr"></span><span id="-p_ptr"></span><span id="-P_PTR"></span>**-p** **** *Ptr*  
Displays all pool allocations that contain the pointer *Ptr*.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Pool instrumentation must be enabled in Win32k.sys in order for this extension to work.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!dpa%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




