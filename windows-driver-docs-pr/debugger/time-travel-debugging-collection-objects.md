---
title: TTD Collection Objects
description: This section describes the range model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# TTD Collection Objects
## Description
*TBD.

## Children

TODO 

| Object | Description |
| --- | --- |
| MinPosition | A [position object](time-travel-debugging-position-objects.md) that describes the earliest position relevant to the range. |




### TTD Collection Object Methods

- ToDo - Move to table?

**Contains(OtherString)** -Method which returns whether the string contains a given sub string.

**EndsWith(OtherString)** -Method which returns whether the string ends with a given string.

**IndexOf(OtherString)** -Method which returns the index of the first occurrence of a substring in the given string.  If no such occurrence exists, -1 is returned.

**LastIndexOf(OtherString)** -Method which returns the index of the last occurrence of a substring in the given string.  If no such occurrence exists, -1 is returned.

**Length** - Property which returns the length of the string.

**PadLeft(TotalWidth)** - Method which right aligns the string to the specified width by inserting spaces at the left of the string.

**PadRight(TotalWidth)** - Method which left aligns the string to the specified width by inserting spaces at the right of the string.

**Remove(StartPos, [Length])** - Method which removes all characters beginning at the specified position from the string.  If an optional length is supplied, only that many characters after the starting position are removed.

**Replace(SearchString, ReplaceString)** - Method which replaces every occurrence of a specified search string with a replacement string.

**StartsWith(OtherString)** - Method which returns whether the string starts with a given string.

**Substring(StartPos, [Length])** - Method which retrieves a substring from the given string.  The substring starts at a specified character position and continues to the end of the string or for the optionally specified length.

**ToLower()** - Returns a copy of this string converted to lowercase.

**ToUpper()** - Returns a copy of this string converted to uppercase.

## Example Usage

*Information pending*



## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
