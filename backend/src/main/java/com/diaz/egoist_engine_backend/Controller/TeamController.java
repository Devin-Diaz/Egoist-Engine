package com.diaz.egoist_engine_backend.Controller;

import com.diaz.egoist_engine_backend.Model.Arc;
import com.diaz.egoist_engine_backend.Model.Team;
import com.diaz.egoist_engine_backend.Service.TeamService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/teams")
public class TeamController {
    private final TeamService teamService;

    public TeamController(TeamService teamService) {
        this.teamService = teamService;
    }

    @GetMapping
    public ResponseEntity<List<Team>> getTeamsByArc(@RequestParam Integer arcId) {
        Optional<Arc> arcOptional = teamService.getArcById(arcId);
        if (arcOptional.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(null);
        }
        Arc arc = arcOptional.get();
        List<Team> teams = teamService.getAllTeamsByArc(arc);
        return ResponseEntity.ok(teams);
    }

}
