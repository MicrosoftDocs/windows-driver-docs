---
title: Advanced SymSrv Use
description: Advanced SymSrv Use
ms.assetid: 16d4dda0-4bcf-4450-9972-e20d71efc845
keywords: ["SymSrv, features", "caching symbols", "symbol servers, caching", "symbols, caching", "symbol servers, downstream store", "downstream store (symbol server)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Advanced SymSrv Use


SymSrv can deliver symbol files from a centralized symbol store. This store can contain any number of symbol files, corresponding to any number of programs or operating systems. The store can also contain binary files (this is useful when debugging minidumps).

The store can contain the actual symbol and binary files, or it can simply contain pointers to symbol files. If the store contains pointers, SymSrv will retrieve the actual files directly from their sources.

SymSrv can also be used to separate a large symbol store into a smaller subset that is appropriate for a specialized debugging task.

Finally, SymSrv can obtain symbol files from an HTTP or HTTPS source using the logon information provided by the operating system. SymSrv supports HTTPS sites protected by smartcards, certificates, and regular logins and passwords. For more information, see [HTTP Symbol Stores](http-symbol-stores.md).

### <span id="setting_the_symbol_path"></span><span id="SETTING_THE_SYMBOL_PATH"></span>Setting the Symbol Path

To use this symbol server, symsrv.dll must be installed in the same directory as the debugger. The symbol path can be set as shown here:

```console
set _NT_SYMBOL_PATH = symsrv*ServerDLL*DownstreamStore*\\Server\Share 

set _NT_SYMBOL_PATH = symsrv*ServerDLL*\\Server\Share 

set _NT_SYMBOL_PATH = srv*DownstreamStore*\\Server\Share 

set _NT_SYMBOL_PATH = srv*\\Server\Share 
```

The parts of this syntax are explained as follows:

<span id="________symsrv"></span><span id="________SYMSRV"></span> **symsrv**  
This keyword must always appear first. It indicates to the debugger that this item is a symbol server, not just a normal symbol directory.

<span id="ServerDLL"></span><span id="serverdll"></span><span id="SERVERDLL"></span>*ServerDLL*  
Specifies the name of the symbol server DLL. If you are using the SymSrv symbol server, this will always be symsrv.dll.

<span id="srv"></span><span id="SRV"></span>**srv**  
This is shorthand for **symsrv\*symsrv.dll**.

<span id="DownstreamStore"></span><span id="downstreamstore"></span><span id="DOWNSTREAMSTORE"></span>*DownstreamStore*  
Specifies the downstream store. This is a local directory or network share that will be used to cache individual symbol files.

You can specify more than one downstream store, separated by asterisks. Multiple downstream stores are explained in **Cascading Downstream Stores** further down on this page.

If you include two asterisks in a row where a downstream store would normally be specified, then the default downstream store is used. This store will be located in the sym subdirectory of the home directory. The home directory defaults to the debugger installation directory; this can be changed by using the [**!homedir**](-homedir.md) extension or by setting the DBGHELP\_HOMEDIR environment variable.

If *DownstreamStore* specifies a directory that does not exist, SymStore will attempt to create it.

If the *DownstreamStore* parameter is omitted and no extra asterisk is included -- in other words, if you use **srv** with exactly one asterisk or **symsrv** with exactly two asterisks -- then no downstream store will be created. The debugger will load all symbol files directly from the server, without caching them locally.

**Note**   If you are accessing symbols from an HTTP or HTTPS site, or if the symbol store uses compressed files, a downstream store is always used. If no downstream store is specified, one will be created in the sym subdirectory of the home directory.

 

<span id="__Server_Share"></span><span id="__server_share"></span><span id="__SERVER_SHARE"></span>*\\\\Server\\Share*  
Specifies the server and share of the remote symbol store.

If a downstream store is used, the debugger will first look for a symbol file in this store. If the symbol file is not found, the debugger will locate the symbol file from the specified *Server* and *Share*, and then cache a copy of this file in the downstream store. The file will be copied to a subdirectory in the tree under *DownstreamStore* which corresponds to its location in the tree under *\\\\Server\\Share*.

The symbol server does not have to be the only entry in the symbol path. If the symbol path consists of multiple entries, the debugger checks each entry for the needed symbol files, in order (from left to right), regardless of whether a symbol server or an actual directory is named.

Here are some examples. To use SymSrv as the symbol server with a symbol store on \\\\mybuilds\\mysymbols, set the following symbol path:

```console
set _NT_SYMBOL_PATH= symsrv*symsrv.dll*\\mybuilds\mysymbols
```

To set the symbol path so that the debugger will copy symbol files from a symbol store on \\\\mybuilds\\mysymbols to your local directory c:\\localsymbols, use:

```console
set _NT_SYMBOL_PATH=symsrv*symsrv.dll*c:\localsymbols*\\mybuilds\mysymbols
```

To set the symbol path so that the debugger will copy symbol files from the HTTP site www.company.com/manysymbols to a local network directory \\\\localserver\\myshare\\mycache, use:

```console
set _NT_SYMBOL_PATH=symsrv*symsrv.dll*\\localserver\myshare\mycache*https://www.company.com/manysymbols
```

This last example can also be shortened as such:

```console
set _NT_SYMBOL_PATH=srv*\\localserver\myshare\mycache*https://www.company.com/manysymbols
```

In addition, the symbol path can contain several directories or symbol servers, separated by semicolons. This allows you to locate symbols from multiple locations (or even multiple symbol servers). If a binary has a mismatched symbol file, the debugger cannot locate it using the symbol server because it checks only for the exact parameters. However, the debugger may find a mismatched symbol file with the correct name, using the traditional symbol path, and successfully load it. Even though the file is technically not the correct symbol file, it might provide useful information.

### <span id="compressed_files"></span><span id="COMPRESSED_FILES"></span>Compressed Files

SymSrv is compatible with symbol stores that contain compressed files, as long as this compression has been done with the compress.exe tool, which is available [here](https://go.microsoft.com/fwlink/p/?linkid=239917). Compressed files should have an underscore as the last character in their file extensions (for example, module1.pd\_ or module2.db\_). For details, see [SymStore](symstore.md).

If the files on the store are compressed, you must use a downstream store. SymSrv will uncompress all files before caching them on the downstream store.

### <span id="deleting_the_cache"></span><span id="DELETING_THE_CACHE"></span>Deleting the Cache

If you are using a *DownstreamStore* as a cache, you can delete this directory at any time to save disk space.

It is possible to have a vast symbol store that includes symbol files for many different programs or Windows versions. If you upgrade the version of Windows used on your target computer, the cached symbol files will all match the earlier version. These cached files will not be of any further use, and therefore this might be a good time to delete the cache.

### <span id="cascading_downstream_stores"></span><span id="CASCADING_DOWNSTREAM_STORES"></span>Cascading Downstream Stores

You can specify any number of downstream stores, separated by asterisks. These stores are known as *cascading symbol stores*.

After the initial **srv\\*** or **symsrv\\**<strong>ServerDLL</strong>*\***, each subsequent token represents a symbol location. The token furthest left is checked first. An empty token -- indicated by two asterisks in a row, or by an asterisk at the end of the string -- represents the default downstream store.

Here is an example of a symbol path that uses two downstream stores to hold information from the main symbol store being accessed. These could be called the master store, the mid-level store, and the local cache:

```console
srv*c:\localcache*\\interim\store*https://msdl.microsoft.com/download/symbols
```

In this scenario, SymSrv will first look in c:\\localcache for a symbol file. If it is found there, it will return a path to it. If it is not found there, it will look in \\\\interim\\store. If the symbol file is found there, SymSrv will copy it to c:\\localcache and return the path. If it is not found there, SymSrv will look in the [Microsoft public symbol store](microsoft-public-symbols.md) at <https://msdl.microsoft.com/download/symbols>; if the file is found there, SymSrv will copy it to both \\\\interim\\store and c:\\localcache.

A similar behavior would be obtained by using the following path:

```console
srv**\\interim\store*https://internetsite
```

In this case, the local cache is the default downstream store and the master store is an internet site. A mid-level store of \\\\interim\\store has been specified for use in between the other two.

When SymSrv processes a path that contains cascading stores, it will skip any store that it cannot read or write to. So if a share goes down, it will copy the file to the store downstream from the missing store without any error. A nice side effect of this error is that the user can specify more than one master store that feeds a single stream of downstream stores as long as the master stores are not writable.

When a compressed symbol file is retrieved from the master store, it will be stored in compressed form in any mid-level store. The file will be uncompressed in the bottom-most store in the path.

### <span id="Working_With_HTTP_and_SMB__Symbol_Server_Paths"></span><span id="working_with_http_and_smb__symbol_server_paths"></span><span id="WORKING_WITH_HTTP_AND_SMB__SYMBOL_SERVER_PATHS"></span>Working With HTTP and SMB Symbol Server Paths

As previously discussed, chaining (or cascading) refers to the copy that occurs between each “\*” separator in the symbol path. The symbols are searched for in a left-to-right order. On each miss, the next (upstream) symbol server is queried, until the file is found.

If found, the file is copied from the (upstream) symbol server to the previous (downstream) symbol server. This is repeated for each (downstream) symbol server. In this way, the (shared) downstream symbol servers are populated with the collective efforts of all clients using the symbol servers.

Even though chained UNC paths can be used without the SRV\* prefix, we recommend that SRV\* be specified so that the advanced error handling of symsrv.dll be used.

When including a HTTP symbol server in the path, only one can be specified (per chain), and it must be at the end of the path (as it can’t be written to serve as a cache). If an HTTP-based symbol store was located in the middle or the left of the store list, it would not be possible to copy any found files to it and the chain would be broken. Furthermore, because the symbol handler cannot open a file from a web site, an HTTP-based store should not be the leftmost or only store on the list. If SymSrv is ever presented with this symbol path, it will attempt to recover by copying the file to the default downstream store and open it from there, regardless of whether the default downstream store is indicated in the symbol path or not.

HTTP is only supported when using the SRV\* prefix (implemented by the symsrv.dll symbol handler).

**Example HTTP and SMB Share Symbol Server Scenarios**

A common UNC-only deployment involves a central office hosting all of the files (\\\\MainOffice\\Symbols), branch offices caching a subset (\\\\BranchOfficeA\\Symbols), and desktops (C:\\Symbols) caching the files that they reference.

```console
srv*C:\Symbols*\\BranchOfficeA\Symbols*\\MainOffice\Symbols
```

When the SMB share is the primary (upstream) symbol store, Read is required.

```console
srv*C:\Symbols*\\MachineName\Symbols
```

When the SMB share is an intermediate (downstream) symbol store, Read/Change is required. The client will copy the file from the primary symbol store to the SMB share, and then from the SMB share to the local folder.

```console
srv*C:\Symbols*\\MachineName\Symbols*https://msdl.microsoft.com/download/symbols
srv*C:\Symbols*\\MachineName\Symbols*\\MainOffice\Symbols
```

When the SMB share is an intermediate (downstream) symbol store in a SymProxy deployment, only Read is required. The SymProxy ISAPI Filter will perform the writes, not the client.

```console
srv*C:\Symbols*\\MachineName\Symbols*https://SymProxyName/Symbols
```

**Multiple HTTP and SMB Share Symbol Server Cache Scenarios**

It is possible to specify multiple chains of symbol servers and cache locations, separated by a semi colon “;”. If the symbols are located in the first chain, the second chain is not traversed. If the symbols are not located in the first chain, the second chain will be traversed and if the symbols are located in the second chain, they will be cached in the specified location. This approach will allow a primary symbol server to normally be used, with a secondary server only being used, if the symbols are not available on the primary symbol server specified in the first chain.

```console
srv*C:\Symbols*\\Machine1\Symbols*https://SymProxyName/Symbols;srv*C:\WebSymbols* https://msdl.microsoft.com/download/symbols
```

### <span id="cache_localsymbolcache"></span><span id="CACHE_LOCALSYMBOLCACHE"></span>cache\**localsymbolcache*

Another way to create a local cache of symbols is by using the **cache\\**<em>*localsymbolcache</em> string in your symbol path. This is not part of the symbol server element, but a separate element in your symbol path. The debugger will use the specified directory *localsymbolcache* to store any symbols loaded from any element that appears in your symbol path to the right of this string. This allows you to use a local cache for symbols downloaded from any location, not just those downloaded by a symbol server.

For example, the following symbol path will not cache symbols taken from *\\\\someshare*. It will use c:\\mysymbols to cache symbols taken from *\\\\anothershare*, because the element beginning with *\\\\anothershare* appears to the right of the **cache\*c:\\mysymbols** element. It will also use c:\\mysymbols to cache symbols taken from the Microsoft public symbol store, because of the usual syntax used by the symbol server (**srv** with two or more asterisks). Moreover, if you subsequently use the [**.sympath+**](-sympath--set-symbol-path-.md) command to add additional locations to this path, these new elements will also be cached, since they will be appended to the right side of the path.

```console
_NT_SYMBOL_PATH=\\someshare\that\cachestar\ignores;srv*c:\mysymbols*https://msdl.microsoft.com/download/symbols;cache*c:\mysymbols;\\anothershare\that\gets\cached
```

### <span id="how_symsrv_locates_files"></span><span id="HOW_SYMSRV_LOCATES_FILES"></span>How SymSrv Locates Files

SymSrv creates a fully qualified UNC path to the desired symbol file. This path begins with the path to the symbol store recorded in the \_NT\_SYMBOL\_PATH environment variable. The **SymbolServer** routine is then used to identify the name of the desired file; this name is appended to the path as a directory name. Another directory name, consisting of the concatenation of the *id*, *two*, and *three* parameters passed to **SymbolServer**, is then appended. If any of these values is zero, they are omitted.

The resulting directory is searched for the symbol file, or a symbol store pointer file.

If this search is successful, **SymbolServer** passes the path to the caller and returns **TRUE**. If the file is not found, **SymbolServer** returns **FALSE**.

### <span id="using_agestore_to_reduce_the_cache_size"></span><span id="USING_AGESTORE_TO_REDUCE_THE_CACHE_SIZE"></span>Using AgeStore to Reduce the Cache Size

The AgeStore tool can be used to delete cached files that are older than a specified date, or to reduce the contents of the cache below a specified size. This can be useful if your downstream store is too large. For details, see [AgeStore](agestore.md).

 

 





