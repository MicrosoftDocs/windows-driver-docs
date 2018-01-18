---
title: findstack
description: The findstack extension locates all of the stacks that contain a specified symbol or module.
ms.assetid: 68a696f1-81fb-401e-ad68-ebc616eaf41a
keywords: ["findstack Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- findstack
api_type:
- NA
---

# !findstack


The **!findstack** extension locates all of the stacks that contain a specified symbol or module.

```
!findstack Symbol [DisplayLevel]
!findstack -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Symbol______"></span><span id="_______symbol______"></span><span id="_______SYMBOL______"></span> *Symbol*   
Specifies a symbol or module.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Specifies what the display should contain. This can be any one of the following values. The default value is 1.

<span id="0"></span>**0**  
Displays only the thread ID for each thread that contains *Symbol*.

<span id="1"></span>**1**  
Displays both the thread ID and the frame for each thread that contains *Symbol*.

<span id="2"></span>**2**  
Displays the entire thread stack for each thread that contains *Symbol*.

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
<td align="left"><p>Uext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about stack traces, see the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands.

Remarks
-------

The [**!stacks**](-stacks.md) kernel-mode extension also display information about stacks, including a brief summary of the state of every thread.

The following are some examples of the output from this extension:

```
0:023> !uext.findstack wininet
Thread 009, 2 frame(s) match
        * 06 03eaffac 771d9263 wininet!ICAsyncThread::SelectThread+0x22a
        * 07 03eaffb4 7c80b50b wininet!ICAsyncThread::SelectThreadWrapper+0xd
 
Thread 011, 2 frame(s) match
        * 04 03f6ffb0 771cda1d wininet!AUTO_PROXY_DLLS::DoThreadProcessing+0xa1
        * 05 03f6ffb4 7c80b50b wininet!AutoProxyThreadFunc+0xb
 
Thread 020, 6 frame(s) match
        * 18 090dfde8 771db73a wininet!CheckForNoNetOverride+0x9c
        * 19 090dfe18 771c5e4d wininet!InternetAutodialIfNotLocalHost+0x220
        * 20 090dfe8c 771c5d6a wininet!ParseUrlForHttp_Fsm+0x135
        * 21 090dfe98 771bcb2c wininet!CFsm_ParseUrlForHttp::RunSM+0x2b
        * 22 090dfeb0 771d734a wininet!CFsm::Run+0x39
        * 23 090dfee0 77f6ad84 wininet!CFsm::RunWorkItem+0x79
 
Thread 023, 9 frame(s) match
        * 16 0bd4fe00 771bd256 wininet!ICSocket::Connect_Start+0x17e
        * 17 0bd4fe0c 771bcb2c wininet!CFsm_SocketConnect::RunSM+0x42
        * 18 0bd4fe24 771bcada wininet!CFsm::Run+0x39
        * 19 0bd4fe3c 771bd22b wininet!DoFsm+0x25
        * 20 0bd4fe4c 771bd706 wininet!ICSocket::Connect+0x32
        * 21 0bd4fe8c 771bd4cb wininet!HTTP_REQUEST_HANDLE_OBJECT::OpenConnection_Fsm+0x391
        * 22 0bd4fe98 771bcb2c wininet!CFsm_OpenConnection::RunSM+0x33
        * 23 0bd4feb0 771d734a wininet!CFsm::Run+0x39
        * 24 0bd4fee0 77f6ad84 wininet!CFsm::RunWorkItem+0x79
 
0:023> !uext.findstack wininet!CFsm::Run 0
Thread 020, 2 frame(s) match
Thread 023, 3 frame(s) match

0:023> !uext.findstack wininet!CFsm 0
Thread 020, 3 frame(s) match
Thread 023, 5 frame(s) match
 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!findstack%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




