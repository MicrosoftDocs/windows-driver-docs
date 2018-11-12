---
title: .quit_lock (Prevent Accidental Quit)
description: The .quit_lock command sets a password to prevent you from accidentally ending the debugging session.
ms.assetid: fd40e642-beba-4da0-a072-6493588980de
keywords: [".quit_lock (Prevent Accidental Quit) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .quit_lock (Prevent Accidental Quit)
api_type:
- NA
ms.localizationpriority: medium
---

# .quit\_lock (Prevent Accidental Quit)


The **.quit\_lock** command sets a password to prevent you from accidentally ending the debugging session.

```dbgcmd
.quit_lock /s NewPassword 
.quit_lock /q Password 
.quit_lock 
```

## <span id="ddk_meta_prevent_accidental_quit_dbg"></span><span id="DDK_META_PREVENT_ACCIDENTAL_QUIT_DBG"></span>Parameters


<span id="________s_NewPassword_____________"></span><span id="________s_newpassword_____________"></span><span id="________S_NEWPASSWORD_____________"></span> **/s** **** *NewPassword*   
Prevents the debugging session from ending and stores *NewPassword*. You cannot end the debugger session until you use the **.quit\_lock /q** command together with this same password. *NewPassword* can be any string. If it contains spaces, you must enclose *NewPassword* in quotation marks.

<span id="________q_Password______________"></span><span id="________q_password______________"></span><span id="________Q_PASSWORD______________"></span> **/q** **** *Password*   
Enables the debugging session to end. *Password* must match the password that you set with the **.quit\_lock /s** command.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Without parameters, **.quit\_lock** displays the current lock status, including the full text of the password.

You can repeat the **.quit\_lock /s** command to change an existing password.

When you use **.quit\_lock /q**, the lock is removed. This command does not close the debugger. Instead, the command only enables you to exit the session in the typical manner when you want to.

**Note**   The password is not "secret". Any remote user who is attached to the debugging session can use **.quit\_lock** to determine the password. The purpose of this command is to prevent accidental use of the [**q (Quit)**](q--qq--quit-.md) command. This command is especially useful if restarting the debugging session might be difficult (for example, during remote debugging).

 

You cannot use the **.quit\_lock /s** command in [Secure Mode](activating-secure-mode.md). If you use this command before Secure Mode is activated, the password protection remains, but you cannot change or remove the password.

 

 





