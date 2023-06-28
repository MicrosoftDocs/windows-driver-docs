---
title: Ambiguous breakpoint resolution
description: Learn more about ambiguous breakpoint resolution
keywords: ["Debugger Engine, breakpoints"]
ms.date: 06/26/2023
---

# Ambiguous breakpoint resolution

In version 10.0.25310.1001 and later of the debugger engine, ambiguous breakpoint resolution is now supported.

Ambiguous breakpoints allow for the debugger to set breakpoints in certain scenarios where a breakpoint expression resolves to multiple locations.  For example, this can happen when:

- Multiple overloads of a function.
- There are multiple symbols that match a breakpoint expression.
- The same symbol name is used for multiple locations.
- The symbol has been inlined.
- Setting a breakpoint in a template function with multiple instantiations in the source window.

When enabled, the debugger will set a breakpoint on each symbol match for a given breakpoint expression. The debugger will also filter symbol matches if certain criteria is met.

For general information about using breakpoints, see [Using Breakpoints](using-breakpoints.md).

## Enabling ambiguous breakpoint resolution

By default, ambiguous breakpoints are disabled. To enable this in a debugger session, run the this command in the WinDbg console:

```dbgcmd
dx @$debuggerRootNamespace.Debugger.Settings.EngineInitialization.ResolveAmbiguousBreakpoints = true;
```

To confirm that the ambiguous breakpoints setting is active:

```dbgcmd
0:010> dx @$debuggerRootNamespace.Debugger.Settings.EngineInitialization.ResolveAmbiguousBreakpoints
@$debuggerRootNamespace.Debugger.Settings.EngineInitialization.ResolveAmbiguousBreakpoints                 : true
```

For more information about using the dx command, see [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md).

To disable the feature, set the above value to be `false`. To make sure that the setting persists across sessions, make sure to click on `File -> Settings -> Debugger Settings` and then check the box marked `Persist engine settings across debugger sessions`.

## Usage applies to single breakpoints

Resolving ambiguous breakpoint expressions only applies to running the breakpoint command to set a single breakpoint in the debugger. In other words, setting multiple breakpoints with the `bm` command will continue to work as usual. Running the command with this feature enabled, will result in new breakpoint behavior for single breakpoints.

For general information about the breakpoint commands, see [bp, bu, bm (Set Breakpoint)](bp--bu--bm--set-breakpoint-.md).

### Hierarchical breakpoints

Hierarchical breakpoints represent the result of resolving an ambiguous breakpoint expression to multiple breakpoints.  If an expression results in two or more matches that will be used to set breakpoints, then another breakpoint is created that will control the breakpoint set. This overriding breakpoint, the hierarchical breakpoint, can be enabled/disabled/cleared and listed just as a normal breakpoint would, with the added functionality of performing the same operation on the breakpoints it owns.

For example, if the command `bp foo!bar` is run, resulting in two matches against the symbol `bar`, then a hierarchical breakpoint will be created that controls the two matches. If the hierarchical is enabled/disabled/cleared, so too will be the matched breakpoints.

The [.bpcmds(Display Breakpoint Commands)](-bpcmds--display-breakpoint-commands-.md) will list the breakpoint command that can be run to set each breakpoint. Breakpoints that are owned by a hierarchical breakpoint will still list a valid bp command that will set a breakpoint on its address. Hierarchical breakpoints will also be listed in the output and will display the command that can be used to recreate the whole set of breakpoints instead of just a single breakpoint.

## Ambiguous symbols

Setting a breakpoint on a symbol name should result in the following behavior if the symbol is:

- An overload: Each overload that matches the symbol should have a breakpoint.

- A template function:
    - If the expression has all template parameters specified (for example `bp foo!bar<int>`), then a breakpoint will be set on the specific implementation of the template function.

    - If the expression has no type implementation specified (for example `bp foo!bar`), then no breakpoints will be set. In this case, `bm` should be used to set breakpoints on the template function.
    - Partial template specifications are not supported by the debugger and no breakpoints will be set in that case.
- An inlined function: Each inlined location has a breakpoint

Note that multiple breakpoints will not be set when the symbol expression includes operators or offsets that require more evaluation by the debugger.  For example, if the symbol `foo` resolves to multiple locations but the expression `foo+5` is evaluated, the debugger will not attempt to resolve all of the locations for breakpoints to be set.

### Breakpoint code examples

Given the following code snippet:

```cpp
class BikeCatalog
{
public:
    void GetNumberOfBikes()
    {
        std::cout << "There are 42 bikes." << std::endl;
    }
    int GetNumberOfBikes(int num)
    {
        std::cout << "There are " << num << " bikes." << std::endl;
        return num;
    }
}; 
```

Invoking the command `bu BikeCatalog::GetNumberOfBikes` would result in two breakpoints being created, one for each overload. Listing the breakpoints would result in the following output:

```dbgcmd
0:000> bl
     2 e Disable Clear  <hierarchical breakpoint>     0001 (0001)  0:**** {BikeCatalog!BikeCatalog::GetNumberOfBikes}
         0 e Disable Clear  00007ff6`c6f52200  [C:\BikeCatalog\BikeCatalog.cpp @ 13]     0001 (0001)  0:**** BikeCatalog!BikeCatalog::GetNumberOfBikes
         1 e Disable Clear  00007ff6`c6f522a0  [C:\BikeCatalog\BikeCatalog.cpp @ 9]     0001 (0001)  0:**** BikeCatalog!BikeCatalog::GetNumberOfBikes

```

## Ambiguous source lines

Setting a breakpoint on a source line should result in the following behavior if the source line is:

- A compiler-optimized function: If the line is split in multiple locations due to compiler optimizations, then a breakpoint will be set on the lowest location within the function corresponding to the specified line.
- An inlined function: A breakpoint is set for each of the call-sites, unless the line specified has been optimized out as part of inlining.
- Resolved to multiple locations: If the above conditions are not met, then a breakpoint will be set for each address with following conditions:
    - If there is a set of _N_ addresses that match the source line in the expression, and a subset _M_ of these _N_ addresses have zero source line displacement from the source line in the expression, then only the _M_ addresses will have breakpoints.
    - If there are no addresses in the set of _N_ addresses that have zero source line displacement from the source line in the expression, then all _N_ addresses will have breakpoints.

## Filtering based on the symbol index

Each symbol should have a unique symbol index. For detailed information about the structure of symbols, see [SYMBOL_INFO structure](/windows/win32/api/dbghelp/ns-dbghelp-symbol_info).

The debugger will use the symbol index to make sure duplicate matches are filtered in the event of multiple addresses with zero source line displacement.

### Examples of template and overloaded functions

#### Template functions

Setting a breakpoint on the source line for the definition of a template function will result in a breakpoint for each implementation of the template function. Given the following template function on line 19 of `BikeCatalog.cpp`:

```cpp
template <class T>
void RegisterBike(T id)
{
    std::cout << "Registered bike " << id << std::endl;
}
```

And its usages:

```cpp
catalog.RegisterBike("gravel bike");
catalog.RegisterBike(1234);
```

Invoking the command ```bp `BikeCatalog.cpp:19` ``` will set two breakpoints that resolve to the implementations of the template function that are used later in the file. If instead the user wanted to set a single breakpoint on the function, they would either have to set a breakpoint on the specific source line of the template function's implementation or set a breakpoint on the symbol of the template function with the appropriate type information (e.g. `bp BikeCatalog::RegisterBike<int>`).

Listing the breakpoints results in the following output:

```dbgcmd
0:000> bl
     2 e Disable Clear  <hierarchical breakpoint>     0001 (0001)  0:**** {BikeCatalog!BikeCatalog::RegisterBike&lt;int&gt;}
         0 e Disable Clear  00007ff7`6b691dd0  [C:\BikeCatalog\BikeCatalog.cpp @ 20]     0001 (0001)  0:**** BikeCatalog!BikeCatalog::RegisterBike<int>
         1 e Disable Clear  00007ff7`6b691e60  [C:\BikeCatalog\BikeCatalog.cpp @ 20]     0001 (0001)  0:**** BikeCatalog!BikeCatalog::RegisterBike<char const *>
```

#### Overloaded functions

Setting a breakpoint on the source line for the definition of an overloaded function will result in only one breakpoint on that definition of the overloaded function. Reusing the code snippet from above, with the first line starting on line 5:

```cpp
class BikeCatalog
{
public:
    void GetNumberOfBikes()
    {
        std::cout << "There are 42 bikes." << std::endl;
    }
    int GetNumberOfBikes(int num)
    {
        std::cout << "There are " << num << " bikes." << std::endl;
        return num;
    }
}; 
```

Invoking the command ```bp `BikeCatalog.cpp:9` ``` will set a single breakpoint on the line for the `void` implementation of `GetNumberOfBikes`. Listing the breakpoints results in the following output:

```dbgcmd
0:000> bl
     0 e Disable Clear  00007ff7`6b691ec0  [C:\BikeCatalog\BikeCatalog.cpp @ 9]     0001 (0001)  0:**** BikeCatalog!BikeCatalog::GetNumberOfBikes
```

#### inlined functions

Setting a breakpoint on the source line for the call-site of an inlined function will result in only one breakpoint on that particular call-site, even if there is another call-site present in the same function.

## Multiple hierarchical breakpoints

Hierarchical breakpoints will own every breakpoint in its set unless:

A breakpoint in its set is cleared

- The hierarchical breakpoint is cleared.
- Another hierarchical breakpoint is created that includes a breakpoint in this hierarchical breakpoint's set.

Another way to think about this is that breakpoints may only have one hierarchical breakpoint owner and that the most recent breakpoint command will determine what the state of the breakpoint list should be.

Furthermore, a hierarchical breakpoint cannot own another hierarchical breakpoint.

### Subsuming pre-existing breakpoints

If a breakpoint _A_ exists on its own and then an ambiguous breakpoint expression is resolved to create breakpoints _A_, _B_, then _A_ will be included in the new breakpoint set with _B_.

### Subsuming hierarchical breakpoint set intersections

If a hierarchical breakpoint _A_ owns breakpoints _B_, _C_ and then an ambiguous breakpoint expression is resolved to create breakpoints:

- _B_, _C_, _D_: Breakpoints _B_, _C_ will join the new hierarchical breakpoint group with breakpoint _D_, and hierarchical breakpoint _A_ will be cleared.

- _C_, _D_ or _B_, _D_: One of the breakpoints will join the new hierarchical breakpoint group with breakpoint _D_, and hierarchical breakpoint _A_ will continue to exist with the one remaining breakpoint that did not join the new group.

## See also

[Using Breakpoints](using-breakpoints.md)

[Breakpoint Syntax](breakpoint-syntax.md)

[bp, bu, bm (Set Breakpoint)](bp--bu--bm--set-breakpoint-.md)

[Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md)
