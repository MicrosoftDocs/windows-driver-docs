---
title: findstack
description: The findstack extension locates all of the stacks that contain a specified symbol or module.
ms.assetid: 68a696f1-81fb-401e-ad68-ebc616eaf41a
keywords: ["findstack Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- findstack
api_type:
- NA
ms.localizationpriority: medium
---

# !findstack


The **!findstack** extension locates all of the stacks that contain a specified symbol or module.

```dbgcmd
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

```dbgcmd
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









