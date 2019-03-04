workflow "Check Home Assistant Configuration" {
  on = "push"
  resolves = ["DEV"]
}

action "STABLE" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    HAVERSION = "STABLE"
  }
}

action "RC" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    HAVERSION = "RC"
  }
  needs = ["STABLE"]
}

action "DEV" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    HAVERSION = "DEV"
  }
  needs = ["RC"]
}
