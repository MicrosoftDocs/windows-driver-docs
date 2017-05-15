---
title: .quit\_lock (Prevent Accidental Quit)
description: The .quit\_lock command sets a password to prevent you from accidentally ending the debugging session.
ms.assetid: fd40e642-beba-4da0-a072-6493588980de
keywords: [".quit_lock (Prevent Accidental Quit) Windows Debugging"]
topic_type:
- apiref
api_name:
- .quit_lock (Prevent Accidental Quit)
api_type:
- NA
---

# .quit\_lock (Prevent Accidental Quit)


The **.quit\_lock** command sets a password to prevent you from accidentally ending the debugging session.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.quit_lock%20%28Prevent%20Accidental%20Quit%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




