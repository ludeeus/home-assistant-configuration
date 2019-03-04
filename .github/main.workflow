workflow "Check Home Assistant Configuration" {
  on = "push"
  resolves = [
    "hmarr/debug-action",
    "hmarr/debug-action@master",
    "hmarr/debug-action@master-1",
  ]
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

action "hmarr/debug-action" {
  uses = "hmarr/debug-action@master"
  needs = ["STABLE"]
}

action "hmarr/debug-action@master" {
  uses = "hmarr/debug-action@master"
  needs = ["RC"]
}

action "hmarr/debug-action@master-1" {
  uses = "hmarr/debug-action@master"
  needs = ["DEV"]
}
