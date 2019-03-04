workflow "Check  HA config" {
  on = "push"
  resolves = [
    "ludeeus/actions/ha-config-chekc@master"]
}

action "ludeeus/actions/ha-config-chekc@master" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    HAVERSION = "DEV"
  }
}
