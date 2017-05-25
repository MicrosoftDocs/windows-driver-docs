---
title: threadtoken
description: The threadtoken extension displays the impersonation state of the current thread.
ms.assetid: df16bdb5-0834-4e07-ad5f-a712f9282bb0
keywords: ["threadtoken Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- threadtoken
api_type:
- NA
---

# !threadtoken


The **!threadtoken** extension displays the impersonation state of the current thread.

``` syntax
!threadtoken
```

## <span id="ddk__threadtoken_dbg"></span><span id="DDK__THREADTOKEN_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ntsdexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about threads and impersonation, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

The **!threadtoken** extension is obsolete in Windows XP and later versions of Windows. Use [**!token**](-token.md) instead.

If the current thread is impersonating, the token that this thread is using will be displayed.

Otherwise, a message reading "Thread is not impersonating" will appear. The process token will then be displayed.

Tokens will be displayed in the same format that [**!handle**](-handle.md) uses when displaying token handles.

Here is an example:

``` syntax
0:000> ~
.  0  id: 1d0.55c   Suspend: 1 Teb 7ffde000 Unfrozen
#  1  id: 1d0.1a4   Suspend: 1 Teb 7ffdd000 Unfrozen

0:000> !threadtoken

***Thread is not impersonating, using process token***
    Auth Id    0 : 0x1c93d
    Type       Primary
    Imp Level  Anonymous
     Token Id  0 : 0x5e8c19
     Mod Id    0 : 0x5e8c12
     Dyn Chg   0x1f4
     Dyn Avail 0x1a4
     Groups    26
     Privs     17
     User      S-1-5-21-2127521184-1604012920-1887927527-74790
     Groups    26
               S-1-5-21-2127521184-1604012920-1887927527-513
               S-1-1-0
               S-1-5-32-544
               S-1-5-32-545
               S-1-5-21-2127521184-1604012920-1887927527-277551
               S-1-5-21-2127521184-1604012920-1887927527-211604
               S-1-5-21-2127521184-1604012920-1887927527-10546
               S-1-5-21-2127521184-1604012920-1887927527-246657
               S-1-5-21-2127521184-1604012920-1887927527-277552
               S-1-5-21-2127521184-1604012920-1887927527-416040
               S-1-5-21-2127521184-1604012920-1887927527-96548
               S-1-5-21-2127521184-1604012920-1887927527-262644
               S-1-5-21-2127521184-1604012920-1887927527-155802
               S-1-5-21-2127521184-1604012920-1887927527-158763
               S-1-5-21-2127521184-1604012920-1887927527-279132
               S-1-5-21-2127521184-1604012920-1887927527-443952
               S-1-5-21-2127521184-1604012920-1887927527-175772
               S-1-5-21-2127521184-1604012920-1887927527-388472
               S-1-5-21-2127521184-1604012920-1887927527-443950
               S-1-5-21-2127521184-1604012920-1887927527-266975
               S-1-5-21-2127521184-1604012920-1887927527-158181
               S-1-5-21-2127521184-1604012920-1887927527-279435
               S-1-5-5-0-116804
               S-1-2-0
               S-1-5-4
               S-1-5-11
     Privileges    17
               SeUndockPrivilege ( Enabled Default )
               SeTakeOwnershipPrivilege ( )
               SeShutdownPrivilege ( )
               SeDebugPrivilege ( )
               SeIncreaseBasePriorityPrivilege ( )
               SeAuditPrivilege ( )
               SeSyncAgentPrivilege ( )
               SeLoadDriverPrivilege ( )
               SeSystemEnvironmentPrivilege ( Enabled )
               SeRemoteShutdownPrivilege ( )
               SeProfileSingleProcessPrivilege ( )
               SeCreatePagefilePrivilege ( )
               SeCreatePermanentPrivilege ( )
               SeSystemProfilePrivilege ( Enabled )
               SeBackupPrivilege ( )
               SeMachineAccountPrivilege ( )
               SeEnableDelegationPrivilege ( Enabled )
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!threadtoken%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




