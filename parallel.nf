

params.check = ""
params.cpus  = 1
params.mem   = "1GB"
params.max_fork = 30
params.out_dir = "output"


cmd_ch = Channel.fromPath(params.script).splitText()


process dorun {
  cpus params.cpus
  memory  params.mem
  maxForks params.max_fork
  input:
     val(cmd) from cmd_ch
  output:
     file("*")
  publishDir params.out_dir
  script:
    """
    $cmd
    """
}
