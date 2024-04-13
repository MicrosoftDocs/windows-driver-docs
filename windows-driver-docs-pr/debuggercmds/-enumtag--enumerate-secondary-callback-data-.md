---
title: ".enumtag (Enumerate Secondary Callback Data)"
description: "The .enumtag command displays secondary bug check callback data and all data tags."
keywords: [".enumtag (Enumerate Secondary Callback Data) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .enumtag (Enumerate Secondary Callback Data)
api_type:
- NA
---

# .enumtag (Enumerate Secondary Callback Data)


The **.enumtag** command displays secondary bug check callback data and all data tags.

```dbgcmd
.enumtag 
```

## <span id="ddk_meta_enumerate_secondary_callback_data_dbg"></span><span id="DDK_META_ENUMERATE_SECONDARY_CALLBACK_DATA_DBG"></span>


## Environment

|  Item       | Description       |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | all              |

 

## Additional Information

For more information and for other ways of displaying this data, see [Reading Bug Check Callback Data](../debugger/reading-bug-check-callback-data.md).

## Remarks

You can use the **.enumtag** command only after a bug check has occurred or when you are debugging a kernel-mode crash dump file.

For each block of secondary bug check callback data, the **.enumtag** command displays the tag (in GUID format) and the data (as bytes and ASCII characters).

Consider the following example.

```dbgcmd
kd> .enumtag
{87654321-0000-0000-0000000000000000} - 0xf9c bytes
  4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00  MZ..............
  B8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00  ........@.......
  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ....
  00 00 00 00 00 00 00 00 00 00 00 00              ............

{12345678-0000-0000-0000000000000000} - 0x298 bytes
  F4 BF 7B 80 F4 BF 7B 80 00 00 00 00 00 00 00 00  ..{...{.........
 4B 44 42 47 98 02 00 00 00 20 4D 80 00 00 00 00  KDBG..... M.....
  54 A5 57 80 00 00 00 00 A0 50 5A 80 00 00 00 00  T.W......PZ.....
 40 01 08 00 18 00 00 00 BC 7D 50 80 00 00 00 00  @........}P.....
  ....
  00 00 00 00 00 00 00 00                          ........
```

In this example, the first batch of secondary data has a GUID ){87654321-0000-0000-0000000000000000}) as its tag, and the second batch of data has a GUID ({12345678-0000-0000-0000000000000000}) as its tag. However, the data is not in a useful format.

