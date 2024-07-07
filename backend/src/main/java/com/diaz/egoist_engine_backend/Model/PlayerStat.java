package com.diaz.egoist_engine_backend.Model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@ToString
@Table(name = "playercareerhistory")
public class PlayerStat {

    @Id
    @Column(name = "player_stat_id")
    private Integer playerStatId;

    @ManyToOne
    @JoinColumn(name = "player_id")
    private Player player;

    @ManyToOne
    @JoinColumn(name = "arc_id")
    private Arc arc;

    @ManyToOne
    @JoinColumn(name = "team_id")
    private Team team;

    @Column(name = "jersey_no")
    private String jerseyNumber;

    @Column(name = "position")
    private String position;

}

