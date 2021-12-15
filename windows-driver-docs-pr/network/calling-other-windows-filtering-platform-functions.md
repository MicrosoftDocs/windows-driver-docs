---
title: Calling Other Windows Filtering Platform Functions
description: Calling Other Windows Filtering Platform Functions
keywords:
- Windows Filtering Platform callout drivers WDK , calling other functions
- callout drivers WDK Windows Filtering Platform , calling other functions
- filter engine WDK Windows Filtering Platform
- kernel-mode callout drivers WDK Windows Filtering Platform
- user-mode callout drivers WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# Calling Other Windows Filtering Platform Functions


Many of the other Windows Filtering Platform functions that are available to user-mode management applications are also available to callout drivers. This enables a callout driver to perform management tasks, such as adding filters to the filter engine. The only difference between the user-mode and kernel-mode versions of these functions is the data type that is returned. The user-mode functions return Win32 error codes, whereas the kernel-mode functions return the equivalent NTSTATUS codes.

Most of the Windows Filtering Platform management functions require a handle to an open session to the filter engine as a parameter. The following topics discuss how a callout driver can open and close a session to the filter engine.

[Opening a Session to the Filter Engine](opening-a-session-to-the-filter-engine.md)

[Closing a Session to the Filter Engine](closing-a-session-to-the-filter-engine.md)

For a list of the other Windows Filtering Platform functions that can be called from a callout driver, see [Other Windows Filtering Platform Functions](calling-other-windows-filtering-platform-functions.md). For more information about how to use these functions, see the [Windows Filtering Platform](/windows/win32/fwp/windows-filtering-platform-start-page) documentation in the Microsoft Windows SDK.

 

