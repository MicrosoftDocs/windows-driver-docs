# Building for OneCore

If you are building user-mode code for Windows 7 and later, including [OneCore](../get-started/what-s-new-in-windows.md) SKUs, you can generate a single binary that works on all of these operating systems.
To do so, link to `onecore_downlevel.lib`.
Some APIs will compile fine but result in stub behavior (including on desktop?).  Some APIs that do not exist on OneCore (for example MessageBox) result in no-op wrappers.

If you want your user mode binary to run only on Windows 10 and later, including OneCore SKUs, link instead to onecore.lib.  You will get a slight load time performance boost.

User-mode code might include: UMDF driver, user-mode DLLs, NT service, console app

The Windows kernel is unchanged in OneCore SKUs, so you don't need to do any special linking if you are building a kernel-mode driver.

The ApiValidator tool in the WDK validates for compiler errors?

You are still restricted to the same subset

Link to list of apis with stub functionality

when to link to onecoreuap.lib vs. onecore.lib

See the requirements block sections of documentation pages to learn which APIs have stubbed behavior when linked to using `onecore_downlevel.lib`.  Also, use runtime testing to verify that your user-mode code runs as you expect on OneCore-based SKUs.
Note that stubbed APIs may generate different error codes.

Related to U category of DCHU (cross-link)

Recommended actions

when building a UMDF driver for 7+, link to onecore_downlevel.  and choose target platform=universal?

See [Validating Universal Windows drivers](validating-universal-drivers.md).
