workflow "Check Home Assistant Configuration" {
  on = "push"
  resolves = ["DEV"]
}

action "STABLE" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    HAVERSION = "STABLE"
    HAALLOWFAIL = "True"
  }
}

action "RC" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    HAVERSION = "RC"
    HAALLOWFAIL = "True"
  }
  needs = ["STABLE"]
}

action "DEV" {
  uses = "ludeeus/actions/ha-config-check@master"
  env = {
    HAVERSION = "DEV"
    HAALLOWFAIL = "True"
  }
  needs = ["RC"]
}
