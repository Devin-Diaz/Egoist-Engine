package com.diaz.egoist_engine_backend.Service;

import com.diaz.egoist_engine_backend.Model.Arc;
import com.diaz.egoist_engine_backend.Model.PlayerStat;
import com.diaz.egoist_engine_backend.Model.Team;
import com.diaz.egoist_engine_backend.Repository.PlayerStatRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class PlayerStatService {
    private final PlayerStatRepository playerStatRepository;

    public PlayerStatService(PlayerStatRepository playerStatRepository) {
        this.playerStatRepository = playerStatRepository;
    }

    public List<PlayerStat> getPlayerStatsByTeam(Team team) {
        return playerStatRepository.findAllByTeam(team);
    }

    public List<PlayerStat> getPlayerStatsByArcAndTeam(Arc arc, Team team) {
        return playerStatRepository.findAllByArcAndTeam(arc, team);
    }

    public Map<Team, List<PlayerStat>> getAllPlayerStatsGroupedByTeam() {
        List<PlayerStat> playerStats = playerStatRepository.findAll();
        return playerStats.stream()
                .collect(Collectors.groupingBy(PlayerStat::getTeam));
    }

}
