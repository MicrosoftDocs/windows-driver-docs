---
title: C28139
description: Warning C28139 The argument should exactly match the type.
ms.assetid: c20b39c2-eee7-4265-ac2f-39023da16549
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28139%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




