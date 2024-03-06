---
title: .copysym (Copy Symbol Files)
description: The .copysym command copies the current symbol files to the specified directory.
keywords: [".copysym (Copy Symbol Files) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .copysym (Copy Symbol Files)
api_type:
- NA
---

# .copysym (Copy Symbol Files)


The **.copysym** command copies the current symbol files to the specified directory.

```dbgsyntax
    .copysym [/l] Path
```

## Parameters


<span id="________l______"></span><span id="________L______"></span> **/l**   
Causes each symbol file to be loaded as it is copied.

<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
Specifies the directory to which the symbol files should be copied. Copies do not overwrite existing files.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

Many times, symbols are stored on a network. The symbol access can often be slow, or you may need to transport your debugging session to another computer where you no longer have network access. In such scenarios, the **.copysym** command can be used to copy the symbols you need for your session to a local directory.

 

 





