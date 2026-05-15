---
title: Managing Minifilter Contexts
description: Defines minifilter context and lists types of minifilter contexts
keywords:
- file system minifilter drivers WDK , contexts
- minifilter drivers WDK , context
- contexts WDK file system minifilter
- contexts WDK file system minifilter , about contexts
ms.date: 12/18/2024
ms.topic: concept-article
---

# Managing minifilter contexts

A *context* is a structure that a minifilter driver defines and that can be associated with a *FltMgr* object.

*FltMgr* provides support that allows minifilter drivers to associate their contexts with *FltMgr*'s objects to preserve state across I/O operations.

## Types of contexts

Minifilters can create and set contexts for the following objects:

- Files (Windows Vista and later)
- Instances
- Streams
- Stream handles (file objects)
- Transactions (Windows Vista and later)
- Volumes

Volume contexts must be allocated from nonpaged pool. All other context types can be allocated from paged or nonpaged pool.

## Context sample code

See the [CTX sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/filesys/miniFilter/ctx) for an example of a minifilter driver that uses contexts.

## How to manage contexts

The following sections describe how to manage filter contexts:

- [Registering Context Types](registering-context-types.md)
- [Creating Contexts](creating-contexts.md)
- [Setting Contexts](setting-contexts.md)
- [Getting Contexts](getting-contexts.md)
- [Referencing Contexts](referencing-contexts.md)
- [Releasing Contexts](releasing-contexts.md)
- [Deleting Contexts](deleting-contexts.md)
- [Freeing Contexts](freeing-contexts.md)
- [File System Support for Contexts](file-system-support-for-contexts.md)
- [Best Practices](best-practices.md)

For information regarding the support provided by *FltMgr*, see [Supporting minifilter contexts](managing-contexts.md).
