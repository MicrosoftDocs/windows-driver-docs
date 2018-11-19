---
title: C28139
description: Warning C28139 The argument should exactly match the type.
ms.assetid: c20b39c2-eee7-4265-ac2f-39023da16549
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28139


warning C28139: The argument should exactly match the type

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Some functions permit limited arithmetic on the argument type, others do not. This usually indicates that an enum formal was not passed a member of the enum, but may be used for other types as well.</p></td>
</tr>
</tbody>
</table>

 

An enumerated value in a function call does not match the type specified for the parameter in the function declaration. This error can occur when parameters are mis-coded, missing, or out of order. Because C permits enumerated values to be used interchangeably, and to be used interchangeably with integer constants, it is not unusual to pass the wrong enumerated value to a function without recognizing the error.

If the Code Analysis tool reports this error, consult the documentation of the function in the WDK. Some functions are coded to permit only enumerated values. Others permit the **?:** operator to select between values of that type, or permit arithmetic on members of the enumerated type, such as when bit flags are encoded as an enumerated value. In a few cases, enumerated values and constants might be combined.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
....KeWaitForSingleObject(&MyMutex, UserRequest, UserRequest, false, NULL);
```

The following code example avoids this warning.

```
....KeWaitForSingleObject(&MyMutex, UserRequest, UserMode, false, NULL);
```

 

 





