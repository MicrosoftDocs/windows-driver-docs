---
title: Deferred Symbol Loading
description: Deferred Symbol Loading
ms.assetid: 58771089-dd0c-4ea9-8a9a-41553f290e88
keywords: ["deferred symbol loading", "symbols, deferred symbol loading", "lazy symbol loading", "symbols, lazy symbol loading"]
---

# Deferred Symbol Loading


## <span id="ddk_deferred_symbol_loading_dbg"></span><span id="DDK_DEFERRED_SYMBOL_LOADING_DBG"></span>


By default, symbol information is not actually loaded when the target modules are loaded. Instead, symbols are loaded by the debugger as they are needed. This is called *deferred symbol loading* or *lazy symbol loading*. When this option is enabled, the debugger loads symbols whenever it encounters an unrecognized symbol.

When the symbol path is changed, for example by using the [**.sympath (Set Symbol Path)**](https://msdn.microsoft.com/library/windows/hardware/ff565407) command, all loaded modules with export symbols are lazily reloaded. Symbols of modules with full PDB symbols will be lazily reloaded if the new path no longer includes the original path that was used to load the PDB symbols. If the new path still includes the original path to the PDB symbol file, those symbols will not be lazily reloaded.

When deferred symbol loading is disabled, process startup can be much slower, because all symbols are read whenever a module is loaded.

In WinDbg, the deferred symbol loading behavior can be modified for symbols that have no module prefix by using the [Resolve Unqualified Symbols](https://msdn.microsoft.com/library/windows/hardware/ff541803) option on the **Debug** menu.

You can override deferred symbol loading by using the [**ld (Load Symbols)**](https://msdn.microsoft.com/library/windows/hardware/ff551979) command or the [**.reload (Reload Module)**](https://msdn.microsoft.com/library/windows/hardware/ff564805) command with the **/f** option. These force the specified symbols to be loaded immediately, although the loading of other symbols is deferred.

By default, deferred symbol loading is enabled. In CDB and KD, the **-s** [command-line option](https://msdn.microsoft.com/library/windows/hardware/ff539174) will turn this option off. It can also be turned off in CDB by using the *LazyLoad* variable in the [tools.ini](configuring-tools-ini.md) file. Once the debugger is running, this option can be turned on or off by using [**.symopt+0x4**](https://msdn.microsoft.com/library/windows/hardware/ff565404) or **.symopt-0x4**, respectively.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Deferred%20Symbol%20Loading%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




