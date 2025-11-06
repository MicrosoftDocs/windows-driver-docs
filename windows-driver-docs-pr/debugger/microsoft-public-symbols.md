---
title: Microsoft Public Symbol Server for Windows Debuggers
description: Learn how to access the Microsoft public symbol server to download Windows debugger symbols. Configure symbol paths and cache symbols locally for faster debugging.
keywords: ["SymSrv, public Microsoft symbols", "symbol servers, public Microsoft symbols", "public symbol store", "Microsoft symbol store"]
ms.date: 11/05/2025
ms.topic: overview
---

# Microsoft public symbol server

**Server Status:** No known issues :white_check_mark:  
The Microsoft public symbol server is fully operational.

Report any known issues to [windbgfb@microsoft.com](mailto:windbgfb@microsoft.com).

---

The Microsoft public symbol server provides free access to Windows debugger symbols, enabling developers to debug Windows applications efficiently. This service allows you to configure symbol paths that automatically download and cache debugging symbols from Microsoft's servers.

Use this guide to quickly set up your symbol server connection and start debugging. You'll learn how to configure paths, cache symbols locally for faster access, and troubleshoot common issues.

## Access the symbol server

You can refer directly to the public symbol server in your symbol path in a number of different ways, described in [Symbol path for Windows debuggers](symbol-path.md).

Quick start options:

- [Set up automatic symbol downloads](#access-the-symbol-server) (recommended for most users)
- [Configure advanced symbol paths](symbol-path.md)
- [Troubleshoot symbol loading issues](using-a-symbol-server.md)

For example, to set the _NT_SYMBOL_PATH environment value, use this command:

```console
set _NT_SYMBOL_PATH=srv*DownstreamStore*https://msdl.microsoft.com/download/symbols
```

*DownstreamStore* must specify a directory on your local computer or network that the debugger uses to cache symbols. This downstream store holds symbols that the debugger accessed. Most symbols that you never access remain on the symbol store at Microsoft. This storage process keeps your downstream store relatively small and allows the symbol server to work quickly, only downloading each file once.

To avoid typing this long symbol path, use the [.symfix (Set symbol store path)](../debuggercmds/-symfix--set-symbol-store-path-.md) command. The following command appends the public symbol store to your existing symbol path:

```dbgcmd
.symfix+ C:\MySymbols
```

If you omit the local symbol cache location, the sym subdirectory of the debugger installation directory is used.

Use the [.sympath (Set symbol store path)](../debuggercmds/-symfix--set-symbol-store-path-.md) command to display the full symbol path. The following example shows how to use symfix to create a local symbol cache and use the Microsoft http symbol server.

```dbgcmd
0: kd> .symfix c:\MyCache
0: kd> .sympath
Symbol search path is: srv*
Expanded Symbol search path is: cache*c:\MyCache;SRV*https://msdl.microsoft.com/download/symbols
```

For more information about working with symbols, see [Using a Symbol Server](using-a-symbol-server.md) and [Symbol path for Windows debuggers](./symbol-path.md).

The public symbol server only supports TLS 1.2+ for https connections.

## Microsoft license terms - Microsoft symbol server

Microsoft makes certain symbols, binary code, and other executables available through the Microsoft symbol server. Use these resources to debug and test your software with Microsoft software. Don't use these resources without authorization. For more information, see the [Microsoft license terms - Microsoft symbol server](/legal/windows-sdk/microsoft-symbol-server-license-terms).

## Troubleshooting

If you encounter connection issues, verify your network supports TLS 1.2+ and check your firewall settings.

## Next steps

Now that you've configured the Microsoft public symbol server, explore these related topics to enhance your debugging workflow:

- **[Symbol path for Windows debuggers](symbol-path.md)** - Learn advanced symbol path configuration options
- **[Using a Symbol Server](using-a-symbol-server.md)** - Discover best practices for symbol server usage
- **[Symbols and Symbol Files](symbols-and-symbol-files.md)** - Understand how debugger symbols work
- **[.symfix command reference](../debuggercmds/-symfix--set-symbol-store-path-.md)** - View complete command syntax and parameters
