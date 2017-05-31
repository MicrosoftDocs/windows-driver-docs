---
title: gs
description: The gs extension analyzes a /GS stack overflow.
ms.assetid: 4c73fd73-e476-4836-80f7-ab9b9c797d8b
keywords: ["gs Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- gs
api_type:
- NA
---

# !gs


The **!gs** extension analyzes a /GS stack overflow.

```
!gs
```

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **!gs**extension helps debug buffer overruns. Run **!gs**when you encounter a STATUS\_STACK\_BUFFER\_OVERRUN error, as the following example shows.

```
0:000> !gs
Corruption occurred in mshtml!CDoc::OnPaint or one of its callers
Real canary not found at 0x74866010
Canary at gsfailure frame 0x292ea4e7
Corrupted canary 0x0013e2c8: 0x00000000
Corrupted cookie value too generic, skipping init bit-flip check
a caller of mshtml!CDoc::OnPaint has corrupted the EBP from 0x0013e254 to 0x0013
e234
check callers (without canary) of mshtml!CDoc::OnPaint for 0x1 bytes of overflow

The canary doesn't look corrupted. Not sure how we got here
EBP/ESP check skipped: No saved EBP in exception context
Function mshtml!CDoc::OnPaint:
  00000000 - 00000004 this                      CDoc*
 0013de40 - 0013e180 rd                        CDoc::OnPaint::__l39::REGION_DAT
A
  0013e180 - 0013e18c Lock                      CDoc::CLock
  0013e18c - 0013e224 DI                        CFormDrawInfo
  0013e23c - 0013e240 hwndInplace               HWND__*
  0013e240 - 0013e244 prc                       tagRECT*
  0013e248 - 0013e250 ptBefore                  tagPOINT
  0013e250 - 0013e254 fViewIsReady              int
  0013e250 - 0013e254 fHtPalette                int
  0013e254 - 0013e258 fNoPaint                  int
  0013e258 - 0013e260 ptAfter                   tagPOINT
  0013e260 - 0013e264 c                         int
  0013e264 - 0013e268 hrgn                      HRGN__*
  0013e268 - 0013e2a8 ps                        tagPAINTSTRUCT
Candidate buffer : ps 0013e268 to 0013e2a7
  0013e268 ea 04 01 a7 00 00 00 00-10 01 00 00 f3 00 00 00 ................
  0013e278 ed 03 00 00 44 02 00 00-84 e5 13 00 f4 e2 13 00 ....D...........
  ...
  0013e2ac 38 20 01 03 10 e3 13 00-68 6b e6 01 d0 e6 03 00 8 ......hk......
 0013e2bc 80 fa 03 00 0d 00 00 00-10 08 19 00 00 00 00 00 ................
0:000>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!gs%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




