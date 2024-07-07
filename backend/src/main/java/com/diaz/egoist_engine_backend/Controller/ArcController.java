package com.diaz.egoist_engine_backend.Controller;

import com.diaz.egoist_engine_backend.Model.Arc;
import com.diaz.egoist_engine_backend.Service.ArcService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/arcs")
public class ArcController {
    private final ArcService arcService;

    public ArcController(ArcService arcService) {
        this.arcService = arcService;
    }

    @GetMapping
    public List<Arc> getAllArcs() {
        return arcService.getAllArcs();
    }
}
