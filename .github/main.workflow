workflow "Check  HA config" {
  on = "push"
  resolves = [
    "ludeeus/actions/ha-config-chekc@master",
    "Debug Action"
  ]
}

action "ludeeus/actions/ha-config-chekc@master" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    VERSION = "DEV"
  }
}

action "Debug Action" {
  uses = "hmarr/debug-action@v1.0.0"
}
