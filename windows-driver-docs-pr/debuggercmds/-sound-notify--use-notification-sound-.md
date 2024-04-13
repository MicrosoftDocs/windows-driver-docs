---
title: ".sound_notify (Use Notification Sound)"
description: "The .sound_notify command causes a sound to be played when WinDbg enters the wait-for-command state."
keywords: [".sound_notify (Use Notification Sound) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .sound_notify (Use Notification Sound)
api_type:
- NA
---

# .sound\_notify (Use Notification Sound)

The **.sound\_notify** command causes a sound to be played when WinDbg enters the wait-for-command state.

```dbgcmd
.sound_notify /ed 
.sound_notify /ef File 
.sound_notify /d 
```

## Parameters

<span id="________ed______"></span><span id="________ED______"></span> **/ed**   
Causes the default Windows alert sound to be played when WinDbg enters the wait-for-command state.

<span id="________ef_______File______"></span><span id="________ef_______file______"></span><span id="________EF_______FILE______"></span> **/ef** **** *File*   
Causes the sound contained in the specified file to be played when WinDbg enters the wait-for-command state.

<span id="________d"></span><span id="________D"></span> **/d**  
Disables the playing of sounds.

## Environment

This command is available only in WinDbg and cannot be used in script files.

| Item      | Description               |
|-----------|---------------------------|
| Modes     | User mode, kernel mode    |
| Targets   | Live, crash dump          |
| Platforms | All                       |
