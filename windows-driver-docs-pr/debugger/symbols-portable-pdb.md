---
title: Portable PDB Symbols
description: The Portable PDB (Program Database) format describes an encoding of debugging information produced by compilers of Common Language Infrastructure languages and consumed by debuggers.
keywords: ["symbols, overview"]
ms.date: 10/12/2020
ms.localizationpriority: medium
---

# Portable PDB Symbols

Starting with version 1.0.2007.01003 of the Windows Debugger, Portable PDB Symbols are supported. Portable symbols can be used to provide information to all of the commonly used debugger commands that use symbols, such as [x (Examine Symbols)](x--examine-symbols-.md), [dt (Display Type)](dt--display-type-.md) and [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md). For general information on the Portable PDB format, see [Portable PDB](https://github.com/dotnet/core/blob/master/Documentation/diagnostics/portable_pdb.md) on GitHub.

## The Portable PDB (Program Database) format

The Portable PDB (Program Database) format describes an encoding of debugging information produced by compilers of Common Language Infrastructure (CLI) languages and consumed by debuggers and other tools. The format is based on the ECMA-335 Partition II metadata standard. It extends its schema while using the same physical table and stream layouts and encodings.

The physical layout of the data is described in the ECMA-335-II Chapter 24 and the Portable PDB debugging metadata format introduces no changes to the fundamental structure. For more information on ECMA-335 see, [Standard ECMA-335 Common Language Infrastructure](https://www.ecma-international.org/publications/standards/Ecma-335.htm).

For complete information on the portable PDB format, see [Portable PDB v1.0: Format Specification](https://github.com/dotnet/runtime/blob/main/docs/design/specs/PortablePdb-Metadata.md).

## Code sample to read portable PDB files

For a code sample that reads portable PDB files, see [Microsoft.DiaSymReader.PortablePdb](https://github.com/dotnet/symreader-portable) on GitHub.

This reader of Portable PDBs implements DiaSymReader interfaces such as ISymUnmanagedReader and ISymUnmanagedBinder. For more information about those .NET interfaces see [Diagnostics Symbol Store (Unmanaged API Reference)](/dotnet/framework/unmanaged-api/diagnostics/).

## See also

[Symbols and Symbol Files](symbols-and-symbol-files.md)

[Public and Private Symbols](public-and-private-symbols.md)
