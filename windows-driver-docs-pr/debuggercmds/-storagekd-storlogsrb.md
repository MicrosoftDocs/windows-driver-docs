---
title: "!storagekd.storlogsrb"
description: "The !storagekd.storlogsrb extension displays the Storport’s internal log entries for the adapter filtered for the Storage (or SCSI) Request Block (SRB) provided."
keywords: ["!storagekd.storlogsrb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- storagekd.storlogsrb
api_type:
- NA
---

# !storagekd.storlogsrb

The **!storagekd.storlogsrb** extension displays the Storport’s internal log entries for the adapter filtered for the Storage (or SCSI) Request Block (SRB) provided.

```dbgcmd
!storagekd.storlogsrb <Address> <srb> [<starting_entry> [<ending_entry>]] [L <count>]
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a Storport adapter device extension or device object.

<span id="_______SRB______"></span><span id="_______srb______"></span> *SRB*   
The SRB to locate.

<span id="_______starting_entry______"></span><span id="_______STARTING_ENTRY______"></span> *starting\_entry*   
The beginning entry in the range to display. If not specified, the last *count* entries will be displayed.

<span id="_______ending_entry______"></span><span id="_______ENDING_ENTRY______"></span> *ending\_entry*   
The ending entry in the range to display. If not specified, *count* entries will be displayed, beginning with the item specified by *starting\_entry*.

<span id="_______count______"></span><span id="_______COUNT______"></span> *count*   
Count of entries to be displayed. If not specified, a value of 50 is used.

## DLL

Storagekd.dll
