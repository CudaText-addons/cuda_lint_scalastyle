Linter for CudaLint plugin.
Supports Scala lexer using Scalastyle.
Requires Java (command "java" must be in the system PATH).

Download Scalastyle .jar file from http://www.scalastyle.org/command-line.html
and write full path to .jar file in [CudaText]/settings/plugins.ini, like this:

[lint_scalastyle]
jar=/home/user/scalastyle_2.12-1.0.0-batch.jar

Scalastyle has the config file scalastyle_config.xml, which is initially
created in the [CudaText]/settings (copied from the plugin folder).

Ported from https://github.com/jawshooah/SublimeLinter-contrib-scalastyle
by Alexey Torgashin (CudaText)
