---
title: Specifying the Source and Target Locations for Device Files
description: Specifying the Source and Target Locations for Device Files
ms.date: 01/21/2022
---

# Specifying the Source and Target Locations for Device Files

When Windows processes copy, rename, and delete file statements in an INF file, it determines the source and target locations for the files. To determine these locations, it examines various INF file sections and entries, including [**SourceDisksNames**](inf-sourcedisksnames-section.md), [**SourceDisksFiles**](inf-sourcedisksfiles-section.md), and [**DestinationDirs**](inf-destinationdirs-section.md).

This page describes how Windows determines source and target locations, and provides guidelines to help you correctly specify these locations.

## Source Media for INF Files

INF files for drivers specify where the files are located by using [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections. The [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections must list all the source media and source files in the driver package except for the catalog and INF files.

Catalog files must be in the same location as the INF file. Catalog files must not be compressed. If the installation media includes multiple disks, then *a separate copy of the INF and catalog files must be included on every disk*. This is because the INF and catalog files must continue to be accessible throughout the entire installation.

[!NOTE] If an INF uses an **Include** directive to reference another INF file, the [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections from the included INF will be folded into this INF, supplementing the sections already present in this INF. However, that should not be relied upon for proper installation of files directly referenced by this INF.  If an INF has a [*CopyFiles*](inf-copyfiles-directive.md) directive for a file, that file should be in the INF's own [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) section.

Decorated [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections take precedence over undecorated sections. For example, a **\[SourceDisksFiles.x86\]** section takes precedence over an undecorated **\[SourceDisksFiles\]** section.

Files referenced by the INF should have file names that are as vendor-specific as possible to avoid potential filename conflicts.

## Target Media for INF Files

An INF file specifies the target location for device files that have a [**DestinationDirs**](inf-destinationdirs-section.md) section. This section should always be specified in the same INF file as the section with the copy, rename, or delete statements.

If an INF has copy, rename, or delete sections but no [**DestinationDirs**](inf-destinationdirs-section.md) section and the INF uses an **Include** directive to include other INF files, Windows searches the included INF files for target location information. However, the order in which Windows searches the included files is not predictable. Therefore, there is a risk that Windows will, for example, copy files to a location not intended by the INF writer. To avoid such confusion, always specify a [**DestinationDirs**](inf-destinationdirs-section.md) section in an INF that lists all copy, rename, or delete sections in that INF.
