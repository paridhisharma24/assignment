package com.project.Controller;

import com.project.Entities.User;
import com.project.Repository.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
public class UserController {
    @Autowired
    private UserRepo userRepository;

    @PostMapping("/signup")
    @ResponseBody
    public User signup(@RequestBody User user) {
        System.out.println("signing up");
        User newUser = new User();

        newUser.setUsername(user.getUsername());
        newUser.setPassword(user.getPassword());
        return userRepository.save(newUser);
    }

    @GetMapping("/login")
    @ResponseBody
    public String login(@RequestBody User user) {
        User existingUser = userRepository.findByUsername(user.getUsername());

        if (existingUser != null && existingUser.getPassword().equals(user.getPassword())) {
            return generateToken(existingUser.getUsername());
        } else {
            throw new IllegalArgumentException("Invalid username or password");
        }
    }

    private String generateToken(String username) {
        // Generate token logic
        return "your_generated_token";
    }
}
