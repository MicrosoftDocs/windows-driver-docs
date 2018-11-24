---
title: Obtaining the Original Source Path of an Installed INF File
description: Obtaining the Original Source Path of an Installed INF File
ms.assetid: 7e086248-b11d-43ee-9afa-fad6f2136dc8
keywords:
- SetupAPI functions WDK , INF files
- paths WDK SetupAPI
- INF files WDK SetupAPI
- source paths WDK INF files
- original source paths WDK INF files
- retrieving INF file path information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining the Original Source Path of an Installed INF File


This topic describes how you can retrieve the original source path of an INF file that is installed in the system INF directory. Although there is no [SetupAPI](setupapi.md) function to perform this retrieval directly, you can perform the retrieval indirectly by including entries in an INF file so that the SetupAPI functions that access INF file entries can be used to retrieve the original source path information from an installed INF file.

This method only works for INF files that are installed in the system INF file directory. You cannot use this method for INF files that are present in the [driver store](driver-store.md).

The co-installer that is provided with the toaster sample in the Windows Driver Kit (WDK) uses this method and this topic includes excerpts from the toaster sample that show this method. For more information about the toaster sample, see *toasterpkg.htm*, which is provided in the *src\\general\\toaster* directory of the WDK.

To use this method to retrieve the original source path of an installed INF file, do the following:

1.  Include in the INF file a section that includes an entry whose first field is the %1% string key token. By default, the %1% string key token represents the original source path of the INF file. When Windows installs such an INF file, it saves the original source path string with the installed version of the INF file. Be aware that this method only works if %1% is used as shown in this example. In general, what %1% resolves to is context-dependent. For example, a %1% field in an *add-registry section* entry does not resolve to the original source path; instead %1% in this context resolves to the path of the corresponding INF file in the [driver store](driver-store.md).

2.  Use **SetupOpenInfFile**, **SetupFindFirstLine**, and **SetupGetStringField** to retrieve the original source path from the entry that includes the %1% string key token.

For example, *toasterpkg.inf* includes the following \[ToasterCoInfo\] section with a custom OriginalInfSourcePath entry whose first field is the %1% string key token.

```cpp
[ToastCoInfo]
; Used by the toaster co-installer to figure out where the original media is
; located (so it can start value-added setup programs).
OriginalInfSourcePath = %1%
```

If an INF is configured as illustrated by the toaster sample, you can then retrieve the original source path after installing the INF file in the system INF directory. To retrieve the original source path, first call **SetupOpenInfFile** to open the installed INF file. For example, the following code example from *toastco.c* opens the installed *toasterpkg.inf* file.

```cpp
// Since the INF is already in %SystemRoot%\Inf, we need to find out where it
// originally came from.  There is no direct way to ascertain an INF&#39;s
// path of origin, but we can indirectly determine it by retrieving a field
// from our INF that uses a string substitution of %1% (DIRID_SRCPATH).
//
hInf = SetupOpenInfFile(DriverInfoDetailData->InfFileName,
                        NULL,
                        INF_STYLE_WIN4,
                        NULL
                        );
```

After opening the installed INF file, call **SetupFindFirstLine** to retrieve the first line of the section that contains the entry whose first field is the %1% string key token. Next, call **SetupGetStringField** to retrieve the first field of this entry and retrieve the original source path of the INF file. For example, the following code example from *toastco.c* retrieves the line that contains the custom OriginalInfSourcePath entry and then retrieves the first field of this entry. Because the first field in the original INF is the %1% string key token, **SetupGetStringField** returns the original source path of the INF file.

```cpp
// Contained within our INF should be a [ToastCoInfo] section with the
// following entry:
//
//     OriginalInfSourcePath = %1%
//
// If we retrieve the value (i.e., field 1) of this line, we&#39;ll get the
// full path where the INF originally came from.
//
if(!SetupFindFirstLine(hInf, L"ToastCoInfo", L"OriginalInfSourcePath", &InfContext)) {
   goto clean0;
}
if(!SetupGetStringField(&InfContext, 1, *MediaRootDirectory, MAX_PATH, &PathLength) ||
  (PathLength <= 1)) {
  goto clean0;
```

 

 





